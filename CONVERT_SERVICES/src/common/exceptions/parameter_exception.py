from src.common.exceptions.convert_services_exception import ConvertServicesException


class ParameterException(ConvertServicesException):
    def __init__(self, message, status, code):
        super().__init__(message, status, code)
