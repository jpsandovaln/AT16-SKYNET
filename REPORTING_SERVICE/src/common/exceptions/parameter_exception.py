from src.common.exceptions.reporting_exception import ReportingException


class ParameterException(ReportingException):
    def __init__(self, message: str, status: str, code: str):
        super().__init__(message, status, code)
