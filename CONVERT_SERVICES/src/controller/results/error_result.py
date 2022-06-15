from src.controller.results.result_convert import ResultConvert


class ErrorResult(ResultConvert):
    def __init__(self, status: str, message: str, code: str):
        super().__init__(status)
        self.message: str = message
        self.code: str = code

    def get_message(self) -> str:
        return self.message

    def get_code(self) -> str:
        return self.code
