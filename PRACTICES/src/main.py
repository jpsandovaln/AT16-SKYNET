from src.state.import_document import ImportantDocument
from src.state.state_object.review_state import ReviewState
from src.state.state_object.progress_state import ProgressState
from src.state.state_object.complete_state import CompleteState
from src.state.state_object.finish_state import FinishState

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

