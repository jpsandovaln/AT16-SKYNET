import abc


class IServer:
    @abc.abstractmethod
    def turn_on(self):
        """Implement turn_on method"""

    @abc.abstractmethod
    def turn_off(self):
        """Implement turn_off method"""

    @abc.abstractmethod
    def open_connection(self):
        """Implement open_connection"""

    @abc.abstractmethod
    def close_connection(self):
        """Implement close_connection"""

    @abc.abstractmethod
    def verify_connection(self):
        """Implement verify_connection"""

    @abc.abstractmethod
    def start_services(self):
        """Implement start_services"""

    @abc.abstractmethod
    def get_log(self):
        """Implement get_log method"""
