import abc


class AbstractClient(abc.ABC):
    @abc.abstractmethod
    def send_message(self, message):
        """ Implement send_message method"""
