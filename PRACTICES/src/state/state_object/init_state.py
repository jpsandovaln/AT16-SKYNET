from src.state.doc_state_interface import IDocState


class InitState(IDocState):
    def display_state(self):
        print("init state")
        print("Document received")
