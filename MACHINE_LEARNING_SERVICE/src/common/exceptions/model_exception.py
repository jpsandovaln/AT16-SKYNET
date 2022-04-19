from src.common.exceptions.machine_learning_exception import MachineLearningException


class ModelException(MachineLearningException):
    def __init__(self, message, status, code, model):
        self.model = model
        super().__init__(message, status, code, model)