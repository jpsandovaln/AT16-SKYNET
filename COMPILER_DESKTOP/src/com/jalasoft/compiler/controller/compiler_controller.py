import requests
from src.com.jalasoft.compiler.view.compiler_view import CompilerView


class CompilerController:
    def __init__(self):
        self.view = CompilerView()
        self.view.init_ui()

        url = "http://127.0.0.1:5000"
        file_path = "D:/EjemploJava8.java"
        files = {'file': open(file_path, 'rb')}
        payload = {'version': '', 'lang': 'java'}
        response = requests.post(url, files=files, data=payload, verify=False)
        resp = response.json()
        message = resp['message']
        self.view.get_main_widget().set_result(message)
