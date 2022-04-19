from src.common.exceptions.reporting_exception import ReportingException


class ParameterException(ReportingException):
    def __init__(self, message, status, code):
        super().__init__(message, status, code)
