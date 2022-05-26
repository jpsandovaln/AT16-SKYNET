from src.controller.results.result_machine_learning import ResultMachineLearning


class SuccessResult(ResultMachineLearning):
    def __init__(self, status: str, message: str):
        super().__init__(status)
        self.message: str = message

    def get_message(self) -> str:
        return self.message