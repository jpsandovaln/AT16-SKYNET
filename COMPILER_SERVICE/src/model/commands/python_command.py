from src.model.command import Command
from src.model.parameter import Parameter


class PythonCommand(Command):
    def build(self, parameter: Parameter) -> str:
        compiler: str = parameter.get_binary_path() + 'python '
        return compiler + parameter.get_file_path()
