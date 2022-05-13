import abc


class IDocState(abc.ABC):
    @abc.abstractmethod
    def display_state(self):
        """ implement display state method """
