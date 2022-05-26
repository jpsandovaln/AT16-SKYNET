from PyQt5.QtWidgets import QPushButton


class PrimaryButton(QPushButton):
    def __init__(self, label):
        super().__init__()
        self.setText(label)
        self.setStyle("background: red")
