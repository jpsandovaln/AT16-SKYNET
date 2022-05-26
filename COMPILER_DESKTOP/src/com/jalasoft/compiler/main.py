import sys
from PyQt5.QtWidgets import QApplication
from src.com.jalasoft.compiler.controller.compiler_controller import CompilerController


if __name__ == "__main__":
    print("hi")
    app = QApplication(sys.argv)
    controller = CompilerController()
    sys.exit(app.exec())
