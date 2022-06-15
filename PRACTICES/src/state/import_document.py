from src.state.doc_state_interface import IDocState
from src.state.state_object.init_state import InitState


class ImportantDocument:
    def __init__(self, title, file_path):
        self.title = title
        self.file_path = file_path
        self._docState: IDocState = InitState()

    def set_state(self, state: IDocState):
        self._docState = state

    def display_state(self):
        self._docState.display_state()

