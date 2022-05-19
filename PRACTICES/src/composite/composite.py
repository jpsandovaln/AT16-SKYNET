from src.composite.product import Product


class CompositeProduct(Product):
    def __init__(self, name):
        super().__init__(name, 0)
        self.product_list = []

    def add_product(self, product):
        self.product_list.append(product)

    def get_price(self):
        price = 0
        for product in self.product_list:
            price = price + product.get_price()
        return price
