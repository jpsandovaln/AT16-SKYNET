from src.controller.results.result_machine_learning import ResultMachineLearning


class SuccessResult(ResultMachineLearning):
    def __init__(self, status, message):
        super().__init__(status)
        self.message = message

    def get_message(self):
        return self.message