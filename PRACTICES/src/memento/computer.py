from src.memento.memento import Memento


class Computer:
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

    def to_string(self):
        print("Computer")
        print("os: " + self.os)
        print("memory: " + self.memory)
        print("hdd: " + self.hdd)

    def backup(self):
        return Memento(self.os, self.memory, self.hdd)

    def restore(self, memento):
        self.os = memento.get_os()
        self.memory = memento.get_memory()
        self.hdd = memento.get_hdd()
