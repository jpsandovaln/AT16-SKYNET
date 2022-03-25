from src.classes.animal import Animal
from src.classes.ave import Ave
from src.classes.pez import Pez


if __name__ == "__main__":
    print(11)
    animal1: Animal = Animal("perro", "blanco") # Animal animal1 = new Animal()
    animal2: Animal = Ave("paloma", "plomo", "pequeño") # Animal animal2 = new Ave()
    animal3: Animal = Pez("pejerrey", "negro") # Animal animal3 = new Pez()
    animalList = [animal1, animal2, animal3]

    for animal in animalList:
        result: str = animal.desplazar()
