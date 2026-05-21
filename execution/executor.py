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

            return None

        if len(response.tool_calls) > 1:

            raise ValueError(
                "Multiple tool calls returned. LOCA currently supports one action per step."
            )

        tool_call = response.tool_calls[0]

        tool_name = tool_call["name"]

        args = tool_call["args"]

        if DEBUG:

            print("\n[EXECUTOR]")
            print(f"Tool: {tool_name}")
