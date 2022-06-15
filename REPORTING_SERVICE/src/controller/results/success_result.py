from src.controller.results.result_reporting import ResultReporting


class SuccessResult(ResultReporting):
    def __init__(self, status: str, message: str):
        super().__init__(status)
        self.message: str = message

    def get_message(self) -> str:
        return self.message