import abc


class AbstractObservableProductNotification(abc.ABC):
    @abc.abstractmethod
    def notify_all_client(self, product, message):
        """Implement notify_all_client method"""

    @abc.abstractmethod
    def add_observer_client(self, product, client):
        """Implement add_observer_client method"""

    @abc.abstractmethod
    def remove_observer_client(self, product, client):
        """Implement remove_observer_client method"""
