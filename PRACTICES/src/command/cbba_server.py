from src.command.server_interface import IServer


class CbbaServer(IServer):
    def turn_on(self):
        print("turn on cbba server")

    def turn_off(self):
        print("turn off cbba server")

    def open_connection(self):
        print("Open connection with cbba server")

    def close_connection(self):
        print("close connection with cbba server")

    def verify_connection(self):
        print("verify connection with cbba server")

    def start_services(self):
        print("start services cbba server")

    def get_log(self):
        print("getting action on cbba server")
