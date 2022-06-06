from abc import ABC, abstractmethod


class Algorithm(ABC):
    @abstractmethod
    def run(self, folder_path, word):
        pass
