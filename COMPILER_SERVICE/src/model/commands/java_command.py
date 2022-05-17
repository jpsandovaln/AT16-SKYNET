import os
from src.model.command import Command
from src.common.exceptions.command_exception import CommandException
from src.model.parameter import Parameter

JAVA_CP_PARAM = ' -cp '
JAVA_AND = ' && '


class JavaCommand(Command):
    def build(self, parameter: Parameter) -> str:
        parameter.validate()
        compiler: str = parameter.get_binary_path() + 'javac '
        execute: str = parameter.get_binary_path() + 'java '
        try:
            basename: str = os.path.basename(parameter.get_file_path())
            simple_name: str = os.path.splitext(basename)[0]
            command: str = compiler + parameter.get_file_path() + JAVA_AND + execute + JAVA_CP_PARAM +\
                parameter.get_folder_path() + ' ' + simple_name
            return command
        except Exception as error:
            raise CommandException(error, '400')
