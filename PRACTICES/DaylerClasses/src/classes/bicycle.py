from .land import Land


class Bicycle(Land):

    def __init__(self, name: str, price: int, has_motor: bool, exercise_bike: bool):
        super().__init__(name, price, has_motor)
        self.exercise_bike = exercise_bike

    def display_data(self) -> str:
        return f''' Name: {self.name}  Price:  {self. price}
        has motor:  {self.has_motor} bicycle: {self.exercise_bike}'''
