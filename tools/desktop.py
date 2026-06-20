import time
import psutil
import pyautogui
import pygetwindow as gw
from pywinauto import Desktop


class DesktopTool:

    def __init__(self):
        pass

    def get_active_window(self):

        try:

            window = gw.getActiveWindow()

            if not window:

                return {
                    "success": False,
                    "title": None
                }

            return {
                "success": True,
                "title": window.title
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    def list_open_apps(self):

        windows = []

        IGNORE = {
