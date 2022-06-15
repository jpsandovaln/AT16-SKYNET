import os
import pathlib
from src.common.exceptions.file_exception import FileException


class FileService:
    @staticmethod
    def get_file_path(file_code, folder_path):
        try:
            pathlib.Path(folder_path).mkdir(parents=True, exist_ok=True)
            file_path = os.path.join(folder_path, file_code.filename)
            file_code.save(file_path)
            return file_path
        except Exception as error:
            raise FileException(error, 404)
