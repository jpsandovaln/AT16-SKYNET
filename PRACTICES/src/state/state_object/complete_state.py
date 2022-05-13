from src.state.doc_state_interface import IDocState


class CompleteState(IDocState):
    def display_state(self):
        print("complete state")
