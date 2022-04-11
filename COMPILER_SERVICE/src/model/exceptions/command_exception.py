class CommandException(Exception):
    def __init__(self, message, status):
        self.message = message
        self.status = status
        self.code = 'AT16-ERR-101'
        super().__init__(self.message)
