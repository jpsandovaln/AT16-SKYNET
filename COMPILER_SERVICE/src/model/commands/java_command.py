import os
from src.model.command import Command

JAVA_COMPILER = 'C:/"Program Files"/Java/jdk1.8.0_251/bin/javac '
JAVA_EXECUTE = 'C:/"Program Files"/Java/jdk1.8.0_251/bin/java '
JAVA_CP_PARAM = ' -cp '
JAVA_AND = ' && '


class JavaCommand(Command):
    def build(self, parameter):
        basename = os.path.basename(parameter.get_file_path())
        simple_name = os.path.splitext(basename)[0]
        command = JAVA_COMPILER + parameter.get_file_path() + JAVA_AND + JAVA_EXECUTE + JAVA_CP_PARAM +\
            parameter.get_folder_path() + ' ' + simple_name
        print(command)
        return command
