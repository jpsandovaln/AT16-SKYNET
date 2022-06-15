class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def generate_command(self):
        return self.strategy.build()
