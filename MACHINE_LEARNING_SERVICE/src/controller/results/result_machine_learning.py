class ResultMachineLearning(object):
    def __init__(self, status: str) -> str:
        self.status: str = status

    def get_status(self):
        return self.status
