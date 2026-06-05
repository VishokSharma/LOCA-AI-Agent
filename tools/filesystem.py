from pathlib import Path
import os

class FileSystemTool:
    def __init__(self):
        pass
    
    def find_file(self, filename):
        try:
            matches = []
            
            for path in Path.home().rglob(filename):
                matches.append(str(path))
                if len(matches) >= 20:
                    break
            return {
                "success": True,
                "matches": matches[:20]
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def find_folder(self, folder_name):
        try:
            matches = []
            
            for path in Path.home().rglob("*"):
                if path.is_dir():
                    if folder_name.lower() in path.name.lower():
                        matches.append(str(path))
                        if len(matches) >= 20:
                            break
            
            return {
                "success": True,
                "matches": matches[:20]
            }
        except Exception as e:
