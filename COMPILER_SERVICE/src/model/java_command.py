import os


class JavaCommand:
    def build(self, file_path, folder_path):
        JAVA_COMPILER = 'C:/"Program Files"/Java/jdk1.8.0_251/bin/javac '
        JAVA_EXECUTE = 'C:/"Program Files"/Java/jdk1.8.0_251/bin/java '
        JAVA_CP_PARAM = ' -cp '
        JAVA_AND = ' && '
        command = JAVA_COMPILER + file_path + JAVA_AND + JAVA_EXECUTE + JAVA_CP_PARAM + folder_path + 'EjemploJava8'
        return command
