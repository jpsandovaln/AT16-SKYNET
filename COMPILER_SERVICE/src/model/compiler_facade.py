from src.model.execute import Execute
from src.model.command_factory import CommandFactory
from src.model.parameter import Parameter
from src.model.command import Command


class CompilerFacade:
    @staticmethod
    def compiler_code(lang: str, file_path: str, upload_dir: str, binary_path: str) -> str:
        parameter: Parameter = Parameter(file_path, upload_dir, binary_path)
        command_factory: CommandFactory = CommandFactory()
        language_instance: Command = command_factory.get_instance(lang)
        command: str = language_instance.build(parameter)
        execute: Execute = Execute()
        return execute.run(command)
