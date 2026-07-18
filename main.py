from tools.browser import BrowserTool
from tools.desktop import DesktopTool
from tools.filesystem import FileSystemTool
from tools.search import SearchTool
from tools.knowledge import KnowledgeTool
from agent.graph import LocaGraph
from langchain_tools.browser_tools import (
    set_browser_tool
)
from langchain_tools.desktop_tools import (
    set_desktop_tool
)
from langchain_tools.filesystem_tools import (
    set_filesystem_tool
)
from langchain_tools.knowledge_tools import (
    set_knowledge_tool
)
from langchain_tools.search_tools import (
    set_search_tool
)

from langchain_tools.all_tools import ALL_TOOLS

from execution.executor import Executor

from llm.groq_client import GroqClient
from llm.planner import Planner
from voice import manager

from dotenv import load_dotenv

import os

load_dotenv()


# =====================================================
# REAL TOOLS
# =====================================================

search = SearchTool()
knowledge = KnowledgeTool()
browser = BrowserTool()
desktop = DesktopTool()
fileSystem = FileSystemTool()
voice = manager.VoiceManager()


# =====================================================
# CONNECT REAL TOOLS TO LANGCHAIN WRAPPERS
# =====================================================

set_filesystem_tool(
    fileSystem
)

set_knowledge_tool(
    knowledge
)

set_search_tool(
    search
)

set_browser_tool(
    browser
)

set_desktop_tool(
    desktop
)


# =====================================================
# MAIN
# =====================================================
mode =2

