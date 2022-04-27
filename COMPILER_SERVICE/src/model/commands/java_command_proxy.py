from src.model.command import Command
from src.model.commands.java_command import JavaCommand
from datetime import datetime
from src.common.exceptions.command_exception import CommandException


class JavaCommandProxy(Command):
    def __init__(self):
        self.java = JavaCommand()

    def build(self, parameter):
        now = datetime.now()
        # database
        if now.hour >= 17:
            command = self.java.build(parameter)
            return command
        raise CommandException('No permission', '403')
