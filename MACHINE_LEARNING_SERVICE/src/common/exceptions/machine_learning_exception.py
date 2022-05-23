class MachineLearningException(Exception):
    def __init__(self, message: str, status: str, code: str, model: str):
        self.message: str = message
        self.status: str = status
        self.code: str = code
        self.model: str = model
        super().__init__(self.message)