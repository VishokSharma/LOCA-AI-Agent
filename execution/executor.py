DEBUG = True


class Executor:

    def __init__(self, tools):

        self.tool_map = {}

        for tool in tools:
            self.tool_map[tool.name] = tool

    def execute(self, response):

        if not response.tool_calls:

            if DEBUG:
                print("[EXECUTOR] No tool calls found")

