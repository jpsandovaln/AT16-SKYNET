from src.common.validator.validator_strategy import ValidatorStrategy
from src.common.exceptions.parameter_exception import ParameterException


class EmptyOrNoneValidator(ValidatorStrategy):
    def __init__(self, field, data):
        self.field = field
        self.data = data

    def validate(self):
        if self.data is None or str(self.data).strip() == "":
            message = "The field: " + self.field + " is invalid"
            raise ParameterException(message, "401", "AT16-ERR-300")
