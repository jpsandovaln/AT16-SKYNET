class Sales:
    def __init__(self, code):
        self.code = code
        self.product_list = []

    def get_code(self):
        return self.code

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)

    def get_total(self):
        total = 0
        for product in self.product_list:
            total = total + product.get_price()
        return total

    def display(self):
        print("------------------------------")
        print("Sales code: " + self.code)
        for product in self.product_list:
            print("Product: " + product.get_name() + " - Price: " + str(product.get_price()))
        print("Total: " + str(self.get_total()))
        print("------------------------------")
