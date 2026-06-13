import json
import re

from playwright.sync_api import sync_playwright

class BrowserTool:

    def __init__(self):
       
        self.playwright = None
        self.context = None
        self.page = None
        self.element_id_map = {}
        
        
    def start_browser(self):

        if self.context is not None:
            return

        self.playwright = sync_playwright().start()

        self.context = self.playwright.chromium.launch_persistent_context(
        user_data_dir="./data/browser_data",
        headless=False
        )

        if self.context.pages:
            self.page = self.context.pages[0]
        else:
            self.page = self.context.new_page()

    def _escape_selector_value(self, value):
        """Safely escape quotes in attribute values for CSS selectors."""
        if not value:
            return value
        return value.replace('"', '\\"')

