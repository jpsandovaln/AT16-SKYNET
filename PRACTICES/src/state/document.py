INIT_STATE = "init"
REVIEW_STATE = "review"
PROGRESS_STATE = "progress"
COMPLETE_STATE = "complete"
FINISH_STATE = "finish"


class Document:
    def __init__(self, title, file_path):
        self.title = title
        self.file_path = file_path
        self.current_state = INIT_STATE

    def set_state(self, state: str):
        self.current_state = state

    def display_state(self):
        if INIT_STATE == self.current_state:
            print("init state")
            print("Document received")
        if REVIEW_STATE == self.current_state:
            print("review state")
            print("send email")
        if PROGRESS_STATE == self.current_state:
            print("progress state")
        if COMPLETE_STATE == self.current_state:
            print("complete state")
