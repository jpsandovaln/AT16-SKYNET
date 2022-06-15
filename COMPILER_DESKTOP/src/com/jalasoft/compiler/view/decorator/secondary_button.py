from PyQt5.QtWidgets import QPushButton
from src.com.jalasoft.compiler.view.decorator.button_component import ButtonComponent


class SecondaryButton(ButtonComponent):
    def __init__(self, label):
        self.button = QPushButton(label)
        self.current_style = "background-color: red; color: black; border-radius: 10px;"
        self.button.setStyleSheet(self.current_style)

    def get_style(self):
        return self.current_style

    def get_button(self):
        return self.button
