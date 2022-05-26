from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPlainTextEdit, QLabel, QLineEdit, QPushButton, \
    QComboBox, QSpacerItem, QSizePolicy, QFileDialog


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
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

        compile_button = QPushButton("Compile")

        vertical_spacer = QSpacerItem(10, 450, QSizePolicy.Expanding)

        parameter_layout = QVBoxLayout()
        parameter_layout.addWidget(QLabel("File path"))
        parameter_layout.addWidget(self.file_path)
        parameter_layout.addWidget(browser_button)
        parameter_layout.addWidget(QLabel("Version"))
        parameter_layout.addWidget(self.version)
        parameter_layout.addWidget(QLabel("Languages"))
        parameter_layout.addWidget(self.languages)
        parameter_layout.addWidget(compile_button)
        parameter_layout.addSpacerItem(vertical_spacer)
        return parameter_layout

    def browse_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\', '')
        self.file_path.setText(file_name[0])

    def set_result(self, message):
        self.result.appendPlainText(message)

    def get_file_path(self):
        return self.file_path

    def get_languages(self):
        return self.languages

    def get_version(self):
        return self.version
