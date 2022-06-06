from src.com.jalasoft.compiler.view.decorator.button_component import ButtonComponent


class ComponentDecorator(ButtonComponent):
    def __init__(self, button_component):
        self.button_component = button_component

    def get_style(self):
        return self.button_component.get_style()

    def get_button(self):
        return self.button_component.get_button()
