from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_tools.all_tools import ALL_TOOLS

load_dotenv()


def main():

    print("=" * 50)
    print("AVAILABLE TOOLS")
    print("=" * 50)

    for tool in ALL_TOOLS:
        print(tool.name)

    print("\n")

    llm = ChatGroq(
        model="qwen/qwen3-32b",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0
    )

    llm_with_tools = llm.bind_tools(
        ALL_TOOLS
    )

    query = """
    Search the web for who created Python.
    """

    print("=" * 50)
    print("QUERY")
    print("=" * 50)
    print(query)

    response = llm_with_tools.invoke(query)

    print("\n")
