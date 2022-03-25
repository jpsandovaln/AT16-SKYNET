from .transport import Transport


class Land(Transport):

    def __init__(self, name: str, price: int, has_motor: bool):
        super().__init__(name, price)
        self.has_motor = has_motor

    def display_data(self) -> str:
        return f"Name: {self.name}, Price: {self.price}, Has Motor: {self.has_motor}"
