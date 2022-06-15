from src.observer.abstract_observable_product_notification import AbstractObservableProductNotification


class ProductNotification(AbstractObservableProductNotification):
    def __init__(self):
        self.client_map = {"car": [], "pc": []}

    def notify_all_client(self, product, message):
        client_list = self.client_map.get(product)
        for client in client_list:
            client.send_message(message)

    def add_observer_client(self, product, client):
        client_list = self.client_map.get(product)
        client_list.append(client)

    def remove_observer_client(self, product, client):
        client_list = self.client_map.get(product)
        client_list.remove(client)
