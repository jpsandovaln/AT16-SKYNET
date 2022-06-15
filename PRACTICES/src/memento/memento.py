class Memento:
    def __init__(self, os, memory, hdd):
        self.os = os
        self.memory = memory
        self.hdd = hdd

    def get_os(self):
        return self.os

    def get_memory(self):
        return self.memory

    def get_hdd(self):
        return self.hdd
