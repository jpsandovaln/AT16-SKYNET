class CShard:
    def __init__(self, file):
        self.file = file

    def create_command_to_execute(self):
        return f"cshard {self.file}"

