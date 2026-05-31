import time

DEBUG = True


class AgentLoop:

    def __init__(
        self,
        planner,
        executor,
        tools
    ):
        self.planner = planner
        self.executor = executor
        self.tools = tools

    def run(self, state):

        print(f"\n[GOAL]\n{state.goal}")

        while True:

            if not DEBUG:
                print(f"\n[STEP {state.step_count}]")

            response = self.planner.plan(state)

            if response is None:

                print("\n[ERROR] Planner returned None")
                break

            if DEBUG:

                print("\n[PLANNER CONTENT]")
                print(response.content)

                print("\n[PLANNER TOOL CALLS]")
                print(response.tool_calls)

            # ==================================================
            # COMPLETION CHECK
            # ==================================================

            if not response.tool_calls:

                print("\n[TASK COMPLETED]")

                print(response.content)

                break
