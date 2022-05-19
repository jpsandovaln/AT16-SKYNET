from src.composite.product import Product


class SoftWare(Product):
    def __init__(self, name, price, type):
        super().__init__(name, price)
        self.type = type

    def get_type(self):
        return self.type
