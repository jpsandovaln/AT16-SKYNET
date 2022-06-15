import os
from PyQt5.QtWidgets import QMenuBar, QMenu, QAction


class MenuBar(QMenuBar):
    def __init__(self):
        super().__init__()
        self.light_style = os.getcwd() + "/../../../../resources/compiler_light.css"
        self.dark_style = os.getcwd() + "/../../../../resources/compiler_dark.css"
        self.create_menu()

    def create_menu(self):
        self.file_menu = QMenu("&Compiler", self)
        self.help_menu = QMenu("&Help", self)
        self.addMenu(self.file_menu)
        self.addMenu(self.help_menu)
        self.addMenu(self.get_setting_menu())

    def get_setting_menu(self):
        self.setting_menu = QMenu("&Setting", self)
        self.style_sub_menu = QMenu("&Style", self)
        self.setting_menu.addMenu(self.style_sub_menu)
        self.dark_action = QAction("&Dark", self)
        self.light_action = QAction("&Light", self)
        self.dark_action.triggered.connect(self.set_dark_action)
        self.light_action.triggered.connect(self.set_light_action)
        self.style_sub_menu.addAction(self.dark_action)
        self.style_sub_menu.addAction(self.light_action)
        return self.setting_menu

    def set_main_widget(self, main_widget):
        self.main_widget = main_widget

    def set_dark_action(self):
        self.main_widget.setStyleSheet(open(self.dark_style).read())

    def set_light_action(self):
        self.main_widget.setStyleSheet(open(self.light_style).read())
