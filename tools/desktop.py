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
            "",
            "Program Manager",
            "Windows Input Experience"
        }

        for window in gw.getAllWindows():

            title = window.title.strip()

            if not title:
                continue

            if title in IGNORE:
                continue

            windows.append(title)

        return {
            "success": True,
            "windows": windows
        }

    def switch_window(self, target):

        target = target.lower()

        for window in gw.getAllWindows():

            if not window.title:
                continue

            if target in window.title.lower():

                try:

                    window.activate()

                    return {
                        "success": True,
                        "window": window.title
                    }

                except Exception as e:

                    return {
                        "success": False,
                        "error": str(e)
                    }

        return {
            "success": False,
            "error": "Window not found"
        }

    def open_app(self, app_name):

        try:

            pyautogui.press("win")

            time.sleep(1)

            pyautogui.write(
                app_name,
                interval=0.03
            )

            time.sleep(1)

            pyautogui.press("enter")

            return {
                "success": True,
                "app": app_name
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    def close_app(self, app_name):

        target = f"{app_name.lower()}.exe"

        killed = 0

        for proc in psutil.process_iter(
            ["pid", "name"]
        ):

            try:

                process_name = proc.info["name"]

                if not process_name:
                    continue

                if process_name.lower() == target:

                    proc.kill()
                    killed += 1

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess
            ):
                continue

        return {
            "success": True,
            "killed": killed
}

    def type_text(self, text):

        try:

            pyautogui.write(
                text,
                interval=0.03
