from src.model.command import Command


class PythonCommand(Command):
    def build(self, parameter):
        return "python " + parameter.get_file_path()
