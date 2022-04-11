class ExecuteException(Exception):
    def __init__(self, message):
        self.message = message
        self.status = '404'
        self.code = 'AT16-ERR-201'
        super().__init__(self.message)
