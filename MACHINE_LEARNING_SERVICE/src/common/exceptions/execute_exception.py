from src.common.exceptions.machine_learning_exception import MachineLearningException


class ExecuteException(MachineLearningException):
    def __init__(self, message: str, status: str, code: str, model: str):
        super().__init__(message, status, code, model)
