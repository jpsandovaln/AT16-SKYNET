from src.model.execute import Execute
from src.model.commands.java_command import JavaCommand
from src.model.commands.python_command import PythonCommand
from src.model.commands.cshard_command_adapter import CShardCommandAdapter
from src.model.parameter import Parameter


class CompilerFacade:
    @staticmethod
    def compiler_code(lang, file_path, upload_dir, binary_path):
        parameter = Parameter(file_path, upload_dir, binary_path)
        if lang == 'java':
            java_command = JavaCommand()
            command = java_command.build(parameter)
        if lang == 'python':
            python_command = PythonCommand()
            command = python_command.build(parameter)
        if lang == 'cshard':
            c_shard = CShardCommandAdapter()
            command = c_shard.build(parameter)
            
        execute = Execute()
        return execute.run(command)
