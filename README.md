# LOCA

<p align="center">
  <img src="https://img.shields.io/badge/python-3.12.1-blue?logo=python&logoColor=white" alt="Python 3.12.1"/>
  <img src="https://img.shields.io/badge/LangGraph-1.2.6-blueviolet?logo=langchain&logoColor=white" alt="LangGraph"/>
  <img src="https://img.shields.io/badge/LLM-Groq-orange?logo=groq&logoColor=white" alt="Groq"/>
  <img src="https://img.shields.io/badge/platform-Windows-0078D6?logo=windows&logoColor=white" alt="Windows"/>
  <img src="https://img.shields.io/badge/voice-Deepgram-13EF93?logo=deepgram&logoColor=white" alt="Deepgram"/>
  <img src="https://img.shields.io/badge/status-active-brightgreen" alt="Status"/>
</p>

> Voice-first autonomous AI agent that plans tool use with LangGraph, executes one action at a time, and operates across browser, desktop, filesystem, search, knowledge, and speech I/O.

---

## Overview

LOCA combines an LLM planner, a single-action executor, and an observation step into a bounded agent loop. The entry point [`main.py`](main.py) wires real tool instances into [`LOCAGraph`](agent/graph.py) and runs them against a Groq-backed chat model.

The agent operates over the browser, local desktop, files, and web search — while also supporting microphone input and spoken output through the `voice/` package. A local Qdrant-backed knowledge store enables document ingestion and semantic retrieval. Prompt-level memory is handled in [`llm/planner.py`](llm/planner.py), which references `user_info.txt` and the knowledge tools for remembered facts and retrieved context.

---

## Key Features

- **LangGraph control flow** — explicit `planner → tool → observe` state transitions compiled in [`agent/graph.py`](agent/graph.py)
- **Single-action enforcement** — [`execution/executor.py`](execution/executor.py) rejects multi-action LLM responses; exactly one tool call per step
- **Browser automation** — Playwright persistent Chromium contexts with stable `element_id` mappings so the LLM acts on integers, not fragile CSS selectors ([`tools/browser.py`](tools/browser.py))
- **Desktop control** — window listing, switching, app launch/kill, typing, hotkeys, and active-window inspection via `pyautogui` / `pywinauto` ([`tools/desktop.py`](tools/desktop.py))
- **Filesystem operations** — recursive search, read/write/append, create file/folder, and directory listing ([`tools/filesystem.py`](tools/filesystem.py))
- **RAG knowledge base** — chunks text, embeds with Ollama `nomic-embed-text`, stores in local Qdrant, and retrieves by semantic similarity ([`rag/`](rag/))
- **Voice I/O** — microphone capture with silence detection, Deepgram STT/TTS, and `pygame` playback coordinated by [`voice/manager.py`](voice/manager.py)
- **Web search** — Tavily-backed online search when the answer is not in memory or local knowledge ([`tools/search.py`](tools/search.py))

---

## Architecture Diagram

```mermaid
graph TD
    Main["main.py · main()"] --> GroqClient["llm/groq_client.py · GroqClient"]
    Main --> Planner["llm/planner.py · Planner"]
    Main --> Executor["execution/executor.py · Executor"]
    Main --> VoiceManager["voice/manager.py · VoiceManager"]
    Main --> LOCAGraph["agent/graph.py · LOCAGraph"]

    LOCAGraph --> PlannerNode["planner_node"]
    LOCAGraph --> ToolNode["tool_node"]
    LOCAGraph --> ObserveNode["observe_node"]

    PlannerNode --> Planner
    Planner --> ChatGroq["ChatGroq · Groq API"]

    ToolNode --> Executor
    Executor --> ToolWrappers["langchain_tools/"]

    subgraph Tools
        ToolWrappers --> BrowserTool["tools/browser.py · BrowserTool"]
        ToolWrappers --> DesktopTool["tools/desktop.py · DesktopTool"]
        ToolWrappers --> FileSystemTool["tools/filesystem.py · FileSystemTool"]
        ToolWrappers --> SearchTool["tools/search.py · SearchTool"]
        ToolWrappers --> KnowledgeTool["tools/knowledge.py · KnowledgeTool"]
    end

    subgraph RAG
