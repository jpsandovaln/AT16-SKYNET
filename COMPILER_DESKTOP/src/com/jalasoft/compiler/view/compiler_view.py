from PyQt5.QtWidgets import QMainWindow
from src.com.jalasoft.compiler.view.menu import MenuBar
from src.com.jalasoft.compiler.view.main_widget import MainWidget


class CompilerView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu_bar = MenuBar()
        self.main_widget = MainWidget()

    def init_ui(self):
        self.setWindowTitle("Compiler Desktop")
        self.setMenuBar(self.menu_bar)
        self.setCentralWidget(self.main_widget)
        self.showMaximized()
        self.show()

    def get_main_widget(self):
        return self.main_widget
