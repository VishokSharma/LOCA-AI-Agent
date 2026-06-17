from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()


class SearchTool:

    def __init__(self):
        self.client = TavilyClient(
            api_key=os.getenv("TAVILY_API_KEY")
        )

    def search(self, query):

