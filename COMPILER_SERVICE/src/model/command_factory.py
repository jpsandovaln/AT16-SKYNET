from src.model.commands.java_command_proxy import JavaCommandProxy
from src.model.commands.java_command import JavaCommand
from src.model.commands.python_command import PythonCommand
from src.model.commands.cshard_command_adapter import CShardCommandAdapter


class CommandFactory:
    def __init__(self):
        self.command_dic = {
            'java': JavaCommand(),
            'python': PythonCommand(),
            'cshard': CShardCommandAdapter(),
            'java-proxy': JavaCommandProxy()
        }
        
    def get_instance(self, lang):
        return self.command_dic.get(lang)
