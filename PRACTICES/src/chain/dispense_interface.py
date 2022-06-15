import abc


class IDispenser(abc.ABC):
    @abc.abstractmethod
    def dispense(self, value):
        """  Implement dispense method """

    @abc.abstractmethod
    def next_chain(self, chain):
        """ Implement next_chain method """
