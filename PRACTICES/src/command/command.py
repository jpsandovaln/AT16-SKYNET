import abc


class Command(abc.ABC):
    def execute(self):
        """Implement execute method"""
