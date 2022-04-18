from src.common.exceptions.reporting_exception import ReportingException


class FilterException(ReportingException):
    def __init__(self, message, status, code):
        super().__init__(message, status, code)