from src.model.command import Command


class PythonCommand(Command):
    def build(self, parameter):
        compiler = parameter.get_binary_path() + 'python '
        return compiler + parameter.get_file_path()
