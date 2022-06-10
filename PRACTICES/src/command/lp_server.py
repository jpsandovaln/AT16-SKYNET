from src.command.server_interface import IServer


class LPServer(IServer):
    def turn_on(self):
        print("turn on La Paz server")

    def turn_off(self):
        print("turn off La Paz server")

    def open_connection(self):
        print("Open connection with La Paz server")

    def close_connection(self):
        print("close connection with La Paz server")

    def verify_connection(self):
        print("verify connection with La Paz server")

    def start_services(self):
        print("start services La Paz server")

    def get_log(self):
        print("getting action on La Paz server")
