import pathlib


class AbsolutePath:
    @staticmethod
    def get_absolute_path():
        absolute_path = pathlib.Path().absolute()
        return absolute_path
