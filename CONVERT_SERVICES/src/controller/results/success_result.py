from src.controller.results.result_convert import ResultConvert


class SuccessResult(ResultConvert):
    def __init__(self, status, message):
        super().__init__(status)
        self.message = message

    def get_message(self):
        return self.message
