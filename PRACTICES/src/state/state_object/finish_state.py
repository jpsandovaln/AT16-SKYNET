from src.state.doc_state_interface import IDocState


class FinishState(IDocState, ):
    def display_state(self):
        print("finish state")
        print("return document")
