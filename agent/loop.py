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

