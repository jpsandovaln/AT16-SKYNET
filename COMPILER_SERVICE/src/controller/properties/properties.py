import os


class Properties:
    @staticmethod
    def get_binary_path(lang, version):
        if lang == 'java':
            return os.getenv('JAVA_BINARY_PATH')
        if lang == 'python':
            return os.getenv('PYTHON_BINARY_PATH')
