from src.state.import_document import ImportantDocument
from src.state.state_object.review_state import ReviewState
from src.state.state_object.progress_state import ProgressState
from src.state.state_object.complete_state import CompleteState
from src.state.state_object.finish_state import FinishState
from src.chain.atm import ATM
from src.composite.software import SoftWare
from src.composite.hardware import HardWare
from src.composite.composite import CompositeProduct
from src.composite.sales import Sales
from src.memento.computer import Computer
from src.memento.caretaker import Caretaker
from src.observer.product_notification import ProductNotification
from src.observer.consumer import Consumer
from src.observer.company import Company


if __name__ == "__main__":
    print(11)
    """ animal1: Animal = Animal("perro", "blanco") # Animal animal1 = new Animal()
    animal2: Animal = Ave("paloma", "plomo", "pequeño") # Animal animal2 = new Ave()
    animal3: Animal = Pez("pejerrey", "negro") # Animal animal3 = new Pez()
    animalList = [animal1, animal2, animal3]

    for animal in animalList:
        result: str = animal.desplazar() """

    """
    document = Document("tesis", "d:/tesis/juanperez.pdf")
    document.display_state()

    document.set_state("review")
    document.display_state()

    document.set_state("progress")
    document.display_state()

    document.set_state("complete")
    document.display_state()
    """
    """
    review_state = ReviewState()
    progress_state = ProgressState()
    complete_state = CompleteState()
    finish_state = FinishState()

    doc = ImportantDocument("tesis", "d:/tesis/juanperez.pdf")
    doc.display_state()

    doc.set_state(review_state)
    doc.display_state()

    doc.set_state(progress_state)
    doc.display_state()

    doc.set_state(complete_state)
    doc.display_state()

    doc.set_state(finish_state)
    doc.display_state()

    doc2 = ImportantDocument("tesis", "d:/tesis/mariavargas.pdf")
    doc2.set_state(review_state)
    """
    """
    atm = ATM(492)
    atm.get_money()
    """
    """
    memory = HardWare("memory", 100, "abc")
    hdd = HardWare("hdd", 200, "xyz")
    motherboard = HardWare("motherboard", 300, "asus")

    cd = SoftWare("windows", 30, "os")

    product_pc1 = CompositeProduct("PC Gamer")
    product_pc1.add_product(memory)
    product_pc1.add_product(motherboard)
    product_pc1.add_product(hdd)

    product_pc2 = CompositeProduct("Pc Personal")
    product_pc2.add_product(memory)
    product_pc2.add_product(hdd)

    product_pc3 = CompositeProduct("Pc Personal plus")
    product_pc3.add_product(memory)
    product_pc3.add_product(hdd)
    product_pc3.add_product(motherboard)
    product_pc3.add_product(cd)

    combo = CompositeProduct("Compo PC")
    combo.add_product(product_pc1)
    combo.add_product(product_pc2)
    combo.add_product(cd)

    sales1 = Sales("X1")
    sales1.add_product(memory)
    sales1.add_product(hdd)
    sales1.add_product(cd)

    sales1.display()

    sales2 = Sales("X2")
    sales2.add_product(memory)

    sales2.display()

    sales3 = Sales("X3")
    sales3.add_product(product_pc1)
    sales3.display()

    sales4 = Sales("X4")
    sales4.add_product(combo)
    sales4.add_product(product_pc2)
    sales4.add_product(motherboard)
    sales4.display()
    """
    """    
    computer = Computer("unix", "16GB", "1TB")
    computer.to_string()
    print("---------------------------")
    computer.os = "win"
    computer.memory = "128MB"
    computer.hdd = "512GB"
    computer.to_string()

    computer2 = Computer("win", "128MB", "512GB")
    computer2.to_string()

    print("+++++++++++++++++++++++++++++")
    computer3 = Computer("unix", "16GB", "1TB")
    computer3.to_string()
    caretaker = Caretaker()
    caretaker.add_computer(1, computer3.backup())

    print("---------------------------")
    computer3.os = "win"
    computer3.memory = "128MB"
    computer3.hdd = "512GB"
    computer3.to_string()
    caretaker.add_computer(2, computer3.backup())

    print("---------------------------")
    computer3.restore(caretaker.get_computer(1))
    computer3.to_string()

    print("---------------------------")
    computer3.restore(caretaker.get_computer(2))
    computer3.to_string()
    """
    ob1 = ProductNotification()
    ob1.add_observer_client("pc", Consumer("Maria", "Arce", "maria@gmail.com"))
    ob1.add_observer_client("pc", Consumer("Carlos", "Lima", "carlos@gmail.com"))

    ob1.add_observer_client("car", Consumer("Pepe", "Vargas", "pepe@gmail.com"))
    ob1.add_observer_client("car", Company("Toyota", 12345688))
    ob1.add_observer_client("car", Consumer("Juan", "Perez", "juan@gmail.com"))

    new_product1 = input("Add Product1: ")
    ob1.notify_all_client(new_product1, "The product is available.")

    new_product2 = input("Add Product2: ")
    ob1.notify_all_client(new_product2, "The product is available.")


