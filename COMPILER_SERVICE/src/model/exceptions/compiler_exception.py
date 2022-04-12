class CompilerException(Exception):
    def __init__(self, message, status, code):
        self.message = message
        self.status = status
        self.code = code
        super().__init__(self.message)
