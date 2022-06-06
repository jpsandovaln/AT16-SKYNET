from PyQt5.QtWidgets import QMainWindow
from view.main_widget import MainWidget


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__main_widget = MainWidget()

    def init_ui(self):
        self.setWindowTitle("Modulo: AT16 PROGRA-102")
        self.setGeometry(1000, 1000, 1000, 1000)
        self.setCentralWidget(self.__main_widget)
        self.showMaximized()
        self.show()

    def get_main_widget(self):
        return self.__main_widget
