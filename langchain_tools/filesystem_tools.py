from langchain.tools import tool

filesystem = None


def set_filesystem_tool(tool_instance):
    global filesystem
    filesystem = tool_instance


@tool
def find_file(filename: str):
    """
    Find a file by name on the system.
    """
    return filesystem.find_file(filename)


@tool
def find_folder(folder_name: str):
    """
    Find a folder by name on the system.
    """
    return filesystem.find_folder(folder_name)


@tool
def list_directory(path: str):
    """
    List files and folders inside a directory.
    """
    return filesystem.list_directory(path)


@tool
