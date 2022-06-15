class ResultReporting(object):
    def __init__(self, status: str):
        self.status: str = status

    def get_status(self) -> str:
        return self.status
