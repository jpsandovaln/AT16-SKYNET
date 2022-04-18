class ReportingException(Exception):
    def __init__(self, message, status, type):
        self.message = message
        self.status = status
        self.type = type
        super().__init__(self.message)