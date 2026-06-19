from langchain.tools import tool

search_tool = None


def set_search_tool(tool_instance):
    global search_tool
    search_tool = tool_instance


@tool
def search(query: str):
    """
