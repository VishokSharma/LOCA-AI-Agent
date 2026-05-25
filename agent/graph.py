from typing import TypedDict, Any
from langgraph.graph import StateGraph, END


class GraphState(TypedDict):
    goal: str
    history: list
    observation: Any
    step_count: int

    response: Any
    result: Any


class LocaGraph:

    def __init__(
        self,
        planner,
        executor,
        tools
    ):
        self.planner = planner
        self.executor = executor
        self.tools = tools

        builder = StateGraph(GraphState)

        builder.add_node(
            "planner",
            self.planner_node
        )

        builder.add_node(
            "tool",
            self.tool_node
