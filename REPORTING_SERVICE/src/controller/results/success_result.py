from src.controller.results.result_reporting import ResultReporting


class SuccessResult(ResultReporting):
    def __init__(self, status, message):
        super().__init__(status)
        self.message = message

    def get_message(self):
        return self.message