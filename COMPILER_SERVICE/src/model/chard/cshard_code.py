class CShard:
    def __init__(self, file: str):
        self.file = file

    def create_command_to_execute(self) -> str:
        return f"cshard {self.file}"

