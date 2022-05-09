import abc
from src.model.parameter import Parameter


class Command(abc.ABC):

    @abc.abstractmethod
    def build(self, parameter: Parameter) -> str:
        """Implement build method"""
