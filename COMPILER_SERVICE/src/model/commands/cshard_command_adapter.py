from src.model.command import Command
from src.model.chard.cshard_code import CShard


class CShardCommandAdapter(Command):
    def build(self, parameter):
        c_shard = CShard(parameter.get_file_path())
        command = c_shard.create_command_to_execute()
        return command
