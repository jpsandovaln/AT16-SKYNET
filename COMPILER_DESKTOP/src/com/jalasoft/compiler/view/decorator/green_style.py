from src.com.jalasoft.compiler.view.decorator.component_decorator import ComponentDecorator


class GreenStyle(ComponentDecorator):
    def __init__(self, button_component):
        super().__init__(button_component)
        self.current_style = super().get_style() + " background-color:green;"
        super().get_button().setStyleSheet(self.current_style)
    
    def get_style(self):
        return self.current_style
    
    def get_button(self):
        return super().get_button()
