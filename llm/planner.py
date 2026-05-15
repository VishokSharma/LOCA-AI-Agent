import json
from langchain_core.prompts import ChatPromptTemplate
DEBUG = True
from langchain_tools.all_tools import ALL_TOOLS
planner_prompt = ChatPromptTemplate.from_template(
    """
    You are an autonomous AI agent capable of using Browser, Desktop, and Filesystem tools.

    ## USER GOAL

    {goal}

    ---

    ## RECENT ACTIONS

    {history}

    ---

    ## CURRENT OBSERVATION

    {observation}

    ---

   
    
Your objective is to achieve the USER GOAL by repeatedly:

1. Analyzing the current observation.
2. Selecting exactly one action.
