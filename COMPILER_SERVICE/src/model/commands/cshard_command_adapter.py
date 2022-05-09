from src.model.command import Command
from src.model.chard.cshard_code import CShard
from src.model.parameter import Parameter


class CShardCommandAdapter(Command):

    def build(self, parameter: Parameter) -> str:
        c_shard: CShard = CShard(parameter.get_file_path())
        command: str = c_shard.create_command_to_execute()
        return command
