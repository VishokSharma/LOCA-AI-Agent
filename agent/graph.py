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
        )

        builder.add_node(
            "observe",
            self.observe_node
        )

        builder.set_entry_point(
            "planner"
        )

        builder.add_conditional_edges(
            "planner",
            self.should_continue,
            {
                "tool": "tool",
                "end": END
            }
        )

        builder.add_edge(
            "tool",
            "observe"
        )

        builder.add_edge(
            "observe",
            "planner"
        )

        self.graph = builder.compile()

    def planner_node(
        self,
        state: GraphState
