from langchain.tools import tool

browser = None


def set_browser_tool(tool_instance):
    global browser
    browser = tool_instance


@tool
def browser_navigate(url: str):
    """
    Navigate the browser to a URL.
    """
    return browser.navigate(url)


@tool
def browser_click(element_id: int):
    """
    Click an element using its element id.
    """
    return browser.click(element_id=element_id)
