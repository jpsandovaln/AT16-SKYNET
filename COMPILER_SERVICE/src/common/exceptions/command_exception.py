from src.common.exceptions.compiler_exception import CompilerException


class CommandException(CompilerException):
    def __init__(self, message, status):
        code = 'AT16-ERR-101'
        super().__init__(message, status, code)
