from langchain.tools import tool

desktop = None


def set_desktop_tool(tool_instance):
    global desktop
    desktop = tool_instance


@tool
def open_app(app_name: str):
    """
    Open a desktop application.
    """
    return desktop.open_app(app_name)


@tool
def close_app(app_name: str):
    """
    Close a desktop application.
    """
    return desktop.close_app(app_name)


@tool
def switch_window(target: str):
    """
    Switch focus to a window.
    """
    return desktop.switch_window(target)


@tool
