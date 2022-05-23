from src.controller.results.result_convert import ResultConvert


class SuccessResult(ResultConvert):
    def __init__(self, status: str, message: str):
        super().__init__(status)
        self.message: str = message

    def get_message(self) -> str:
        return self.message
