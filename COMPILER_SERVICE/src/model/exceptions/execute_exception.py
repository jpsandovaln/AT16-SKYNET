from src.model.exceptions.compiler_exception import CompilerException


class ExecuteException(CompilerException):
    def __init__(self, message):
        status = '404'
        code = 'AT16-ERR-201'
        super().__init__(message, status, code)
