import abc


class Command(abc.ABC):

    @abc.abstractmethod
    def build(self, parameter):
        """Implement build method"""
