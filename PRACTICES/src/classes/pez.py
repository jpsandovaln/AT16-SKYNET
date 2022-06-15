from src.classes.animal import Animal


class Pez(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def desplazar(self):
        print(self.name + " = nadando")
        self._comer()

    def _comer(self):
        print("planton")
