from src.model.execute import Execute
from src.model.command_factory import CommandFactory
from src.model.parameter import Parameter


class CompilerFacade:
    @staticmethod
    def compiler_code(lang, file_path, upload_dir, binary_path):
        parameter = Parameter(file_path, upload_dir, binary_path)
        command_factory = CommandFactory()
        language_instance = command_factory.get_instance(lang)
        command = language_instance.build(parameter)
        execute = Execute()
        return execute.run(command)
