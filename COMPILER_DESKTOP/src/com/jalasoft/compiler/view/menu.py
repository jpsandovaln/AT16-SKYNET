from PyQt5.QtWidgets import QMenuBar, QMenu


class MenuBar(QMenuBar):
    def __init__(self):
        super().__init__()
        self.create_menu()

    def create_menu(self):
        file_menu = QMenu("&Compiler", self)
        help_menu = QMenu("&Help", self)
        self.addMenu(file_menu)
        self.addMenu(help_menu)
