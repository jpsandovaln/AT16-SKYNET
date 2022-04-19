class MachineLearningException(Exception):
    def __init__(self, message, status, code, model):
        self.message = message
        self.status = status
        self.code = code
        self.model = model
        super().__init__(self.message)