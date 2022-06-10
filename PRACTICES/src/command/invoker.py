class Invoker:
    def __init__(self, command):
        self.command = command

    def run(self):
        self.command.execute()
