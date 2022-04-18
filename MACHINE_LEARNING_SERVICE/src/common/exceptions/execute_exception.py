from src.common.exceptions.machine_learning_exception import MachineLearningException


class ExecuteException(MachineLearningException):
    def __init__(self, message, status, code):
        super().__init__(message, status, code)
