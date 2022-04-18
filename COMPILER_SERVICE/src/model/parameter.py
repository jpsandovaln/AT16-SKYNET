import os
from src.common.exceptions.parameter_exception import ParameterException


class Parameter:
    def __init__(self, file_path, folder_path, binary_path):
        self.file_path = file_path
        self.folder_path = folder_path
        self.binary_path = binary_path

    def get_file_path(self):
        return self.file_path

    def get_folder_path(self):
        return self.folder_path

    def get_binary_path(self):
        return self.binary_path

    def validate(self):
        if self.file_path is None or str(self.file_path).strip() == "":
            raise ParameterException("Invalid file, the value is empty", "401", "AT16-ERR-300")

        if self.folder_path is None or str(self.folder_path).strip() == "":
            raise ParameterException("Invalid folder, the value is empty", "401", "AT16-ERR-301")

        if self.binary_path is None or str(self.binary_path).strip() == "":
            raise ParameterException("Invalid binary folder, the value is empty", "401", "AT16-ERR-302")

        is_file = os.path.isfile(self.file_path)
        if not is_file:
            raise ParameterException("It is not file", "402", "AT16-ERR-305")

        is_folder = os.path.isdir(self.folder_path)
        if not is_folder:
            raise ParameterException("it is not folder", "402", "AT16-ERR-306")
