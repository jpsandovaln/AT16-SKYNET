from src.model.command import Command
from src.model.commands.java_command import JavaCommand
from datetime import datetime
from src.common.exceptions.command_exception import CommandException
from src.model.parameter import Parameter


class JavaCommandProxy(Command):
    def __init__(self):
        self.java: JavaCommand = JavaCommand()

    def build(self, parameter: Parameter) -> str:
        now: any = datetime.now()
        if now.hour >= 17:
            command: str = self.java.build(parameter)
            return command
        raise CommandException('No permission', '403')
