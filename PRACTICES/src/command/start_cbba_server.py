from src.command.command import Command


class StartCbbaServer(Command):
    def __init__(self, server):
        self.server = server

    def execute(self):
        self.server.open_connection()
        self.server.verify_connection()
        self.server.turn_on()
        self.server.start_services()
        self.server.get_log()
        self.server.close_connection()
