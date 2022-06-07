import abc


class BuilderPizza(abc.ABC):
    @abc.abstractmethod
    def build(self):
        """Implement build method"""
