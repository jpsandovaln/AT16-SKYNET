from src.model.exceptions.compiler_exception import CompilerException


class ParameterException(CompilerException):
    def __init__(self, message, status, code):
        super().__init__(message, status, code)
