import os
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPlainTextEdit, QLabel, QLineEdit, QPushButton, \
    QComboBox, QSpacerItem, QSizePolicy, QFileDialog
from src.com.jalasoft.compiler.view.decorator.primary_button import PrimaryButton
from src.com.jalasoft.compiler.view.decorator.secondary_button import SecondaryButton
from src.com.jalasoft.compiler.view.decorator.green_style import GreenStyle
from src.com.jalasoft.compiler.view.decorator.border_style import BorderStyle

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.style = os.getcwd() + "/../../../../resources/compiler_light.css"
        self.setStyleSheet(open(self.style).read())
        self.layout = QHBoxLayout()
        self.layout.addLayout(self.get_left_layout(), 25)
        self.result = QPlainTextEdit()
        self.layout.addWidget(self.result, 75)
        self.setLayout(self.layout)

    def get_left_layout(self):
        self.file_path = QLineEdit()
        self.file_path.setReadOnly(True)
        browser_button = QPushButton("Browse")
        browser_button.clicked.connect(self.browse_file)

        self.version = QLineEdit()

        self.languages = QComboBox()
        self.languages.addItem("java")
        self.languages.addItem("python")
        self.languages.addItem("java-proxy")

        self.compile_button = QPushButton("Compile")

        vertical_spacer = QSpacerItem(10, 450, QSizePolicy.Expanding)

        parameter_layout = QVBoxLayout()
        parameter_layout.addWidget(QLabel("File path"))
        parameter_layout.addWidget(self.file_path)
        parameter_layout.addWidget(browser_button)
        parameter_layout.addWidget(QLabel("Version"))
        parameter_layout.addWidget(self.version)
        parameter_layout.addWidget(QLabel("Languages"))
        parameter_layout.addWidget(self.languages)
        parameter_layout.addWidget(self.compile_button)
        parameter_layout.addSpacerItem(vertical_spacer)

        accept = PrimaryButton("Accept")
        cancel = SecondaryButton("Cancel")

        parameter_layout.addWidget(accept.get_button())
        parameter_layout.addWidget(cancel.get_button())

        accept_2 = GreenStyle(PrimaryButton("Accept 2"))
        accept_3 = BorderStyle(GreenStyle(PrimaryButton("Accept 3")))
        accept_4 = BorderStyle(PrimaryButton("Accept 4"))

        parameter_layout.addWidget(accept_2.get_button())
        parameter_layout.addWidget(accept_3.get_button())
        parameter_layout.addWidget(accept_4.get_button())

        return parameter_layout

    def browse_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\', '')
        self.file_path.setText(file_name[0])

    def set_result(self, message):
        self.result.appendPlainText(message)

    def get_file_path(self):
        return str(self.file_path.text())

    def get_languages(self):
        return str(self.languages.currentText())

    def get_version(self):
        return str(self.version.text())

    def get_compiler_button(self):
        return self.compile_button
