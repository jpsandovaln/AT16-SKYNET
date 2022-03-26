from .land import Land


class Car(Land):

    def __init__(self, name: str, price: int, has_motor: bool, use_gas: bool):
        super().__init__(name, price, has_motor)
        self.use_gas = use_gas

    def display_data(self) -> str:
        return f'''Name:  {self.name}  Price:   {self.price}
            has motor:   {self.has_motor}  bicycle:  {self.use_gas}'''
