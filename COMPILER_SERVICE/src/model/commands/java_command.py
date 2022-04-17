import os
from src.model.command import Command
from src.common.exceptions.command_exception import CommandException

JAVA_CP_PARAM = ' -cp '
JAVA_AND = ' && '


class JavaCommand(Command):
    def build(self, parameter):
        parameter.validate()
        compiler = parameter.get_binary_path() + 'javac '
        execute = parameter.get_binary_path() + 'java '
        try:
            basename = os.path.basename(parameter.get_file_path())
            simple_name = os.path.splitext(basename)[0]
            command = compiler + parameter.get_file_path() + JAVA_AND + execute + JAVA_CP_PARAM +\
                parameter.get_folder_path() + ' ' + simple_name
            return command
        except Exception as error:
            raise CommandException(error, '400')
