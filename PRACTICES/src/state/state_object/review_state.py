from src.state.doc_state_interface import IDocState


class ReviewState(IDocState):
    def display_state(self):
        print("review state")
        print("send email")
