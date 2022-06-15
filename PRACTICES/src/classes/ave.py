from src.classes.animal import Animal


class Ave(Animal):
    def __init__(self, name, color, type):
        super().__init__(name, color)
        self.type = type

    def desplazar(self):
        return 1
        print(self.name + " = volando")
