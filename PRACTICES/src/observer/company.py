from src.observer.abstract_client import AbstractClient


class Company(AbstractClient):
    def __init__(self, name, cellphone):
        self.name = name
        self.cellphone = cellphone

    def get_name(self):
        return self.name

    def get_cellphone(self):
        return self.cellphone

    def send_message(self, message):
        print("---------------------------------")
        print("Sending message to company: " + self.name)
        print("Whatsapp: " + str(self.cellphone))
        print("message: " + message)
        print("---------------------------------")
