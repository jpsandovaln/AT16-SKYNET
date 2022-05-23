from src.common.exceptions.machine_learning_exception import MachineLearningException


class ModelException(MachineLearningException):
    def __init__(self, message: str, status: str, code: str, model: str):
        self.model: str = model
        super().__init__(message, status, code, model)