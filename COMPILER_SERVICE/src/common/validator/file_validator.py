import os
from src.common.validator.validator_strategy import ValidatorStrategy
from src.common.exceptions.parameter_exception import ParameterException


class FileValidator(ValidatorStrategy):
    def __init__(self, data, is_file):
        self.data = data
        self.is_file = is_file
    
    def validate(self):
        if self.is_file:
            is_file: bool = os.path.isfile(self.data)
            if not is_file:
                raise ParameterException("Invalid file", "402", "AT16-ERR-305")
        else:
            is_folder: bool = os.path.isdir(self.data)
            if not is_folder:
                raise ParameterException("Invalid folder", "402", "AT16-ERR-306")
