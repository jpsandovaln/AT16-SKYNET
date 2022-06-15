import abc


class ButtonComponent(abc.ABC):
    @abc.abstractmethod
    def get_style(self):
        """Implement get_style method"""

    @abc.abstractmethod        
    def get_button(self):
        """Implement get_button method"""
