from src.composite.product import Product


class HardWare(Product):
    def __init__(self, name, price, branch):
        super().__init__(name, price)
        self.branch = branch

    def get_branch(self):
        return self.branch
