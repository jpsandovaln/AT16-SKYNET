from src.controller.results.result_reporting import ResultReporting


class ErrorResult(ResultReporting):
    def __init__(self, status, message, code):
        super().__init__(status)
        self.message = message
        self.code = code

    def get_message(self):
        return self.message

    def get_code(self):
        return self.code