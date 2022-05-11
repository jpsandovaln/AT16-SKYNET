class Context:
    def __init__(self, strategies: list):
        self.strategies: list = strategies

    def validate(self):
        for strategy in self.strategies:
            strategy.validate()
