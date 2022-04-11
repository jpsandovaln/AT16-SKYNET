from src.controller.result.result_compiler import ResultCompiler


class SuccessResult(ResultCompiler):
    def __init__(self, status, message):
        super().__init__(status)
        self.message = message

    def get_message(self):
        return self.message
