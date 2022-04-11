from src.model.command import Command

PYTHON_COMPILER = 'C:/python39/python '


class PythonCommand(Command):
    def build(self, parameter):
        return PYTHON_COMPILER + parameter.get_file_path()
