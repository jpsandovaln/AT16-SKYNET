from src.common.validator.validator_strategy import ValidatorStrategy


class DateValidator(ValidatorStrategy):
    def __init__(self, date):
        self.date = date
        
    def validate(self):
        pass
