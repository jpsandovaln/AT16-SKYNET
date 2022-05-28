import requests
from src.com.jalasoft.compiler.view.compiler_view import CompilerView


class CompilerController:
    def __init__(self):
        self.view = CompilerView()
        self.view.init_ui()
        self.view.get_main_widget().get_compiler_button().clicked.connect(self.show_data)

    def show_data(self):
        url = "http://127.0.0.1:5000"
        file_path = self.view.get_main_widget().get_file_path()
        lang = self.view.get_main_widget().get_languages()
        version = self.view.get_main_widget().get_version()

        files = {'file': open(file_path, 'rb')}
        payload = {'version': version, 'lang': lang}
        response = requests.post(url, files=files, data=payload, verify=False)
        resp = response.json()
        message = resp['message']
        self.view.get_main_widget().set_result(message)
