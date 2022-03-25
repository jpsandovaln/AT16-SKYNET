class Transport:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> int:
        return self.price


