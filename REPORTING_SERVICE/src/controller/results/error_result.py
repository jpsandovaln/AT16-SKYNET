from src.controller.results.result_reporting import ResultReporting


class ErrorResult(ResultReporting):
    def __init__(self, status: str, message: str, code: str):
        super().__init__(status)
        self.message: str = message
        self.code: str = code

    def get_message(self) -> str:
        return self.message

    def get_code(self) -> str:
        return self.code