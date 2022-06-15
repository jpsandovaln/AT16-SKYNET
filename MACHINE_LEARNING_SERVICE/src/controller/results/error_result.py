from src.controller.results.result_machine_learning import ResultMachineLearning


class ErrorResult(ResultMachineLearning):
    def __init__(self, status, message, code):
        super().__init__(status)
        self.message = message
        self.code = code

    def get_message(self):
        return self.message

    def get_code(self):
        return self.code