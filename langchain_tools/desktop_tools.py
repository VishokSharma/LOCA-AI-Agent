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
def get_active_window():
    """
    Get the currently active window.
    """
    return desktop.get_active_window()


@tool
def list_open_apps():
    """
    List all currently open windows.
    """
    return desktop.list_open_apps()


@tool
def type_text(text: str):
    """
    Type text into the active window.
    """
    return desktop.type_text(text)


@tool
def press_key(key: str):
    """
    Press a keyboard key.
    """
    return desktop.press_key(key)


@tool
def hotkey(keys: list[str]):
    """
    Press a keyboard shortcut.
