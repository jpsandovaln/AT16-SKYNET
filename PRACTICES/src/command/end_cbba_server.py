from src.command.command import Command


class EndCbbaServer(Command):
    def __init__(self, server):
        self.server = server

    def execute(self):
        self.server.open_connection()
        self.server.turn_off()
        self.server.close_connection()
