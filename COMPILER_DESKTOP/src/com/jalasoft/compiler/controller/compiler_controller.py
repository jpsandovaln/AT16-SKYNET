from src.com.jalasoft.compiler.view.compiler_view import CompilerView


class CompilerController:
    def __init__(self):
        self.view = CompilerView()
        self.view.init_ui()
