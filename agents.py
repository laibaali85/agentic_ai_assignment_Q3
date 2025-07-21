

class Agent:
    def __init__(self, name, goal, handle):
        self.name = name
        self.goal = goal
        self.handle = handle

class Runner:
    @staticmethod
    def run(agent, input_data):
        print(f"Running agent: {agent.name}")
        return agent.handle(input_data)
