from langchain.tools import tool

knowledge = None


def set_knowledge_tool(tool_instance):
    global knowledge
    knowledge = tool_instance


@tool
def add_document(path: str):
    """
    Add a document to the knowledge base.
    The document will be chunked, embedded and stored in Qdrant.
    """
    return knowledge.add_document(path)


@tool
