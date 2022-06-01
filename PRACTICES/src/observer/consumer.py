from src.observer.abstract_client import AbstractClient


class Consumer(AbstractClient):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def send_message(self, message):
        print("---------------------------------------")
        print("Sending message to consumer: " + self.first_name + " - " + self.last_name)
        print("email: " + self.email)
        print("message: " + message)
        print("---------------------------------------")
