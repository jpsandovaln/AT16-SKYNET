from src.state.doc_state_interface import IDocState


class ProgressState(IDocState):
    def display_state(self):
        print("progress state")
