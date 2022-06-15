class Caretaker:
    def __init__(self):
        self.pc_dic = {}

    def add_computer(self, key, memento):
        self.pc_dic[key] = memento

    def get_computer(self, key):
        return self.pc_dic.get(key)
