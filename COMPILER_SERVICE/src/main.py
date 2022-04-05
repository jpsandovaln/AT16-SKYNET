import os
import pathlib
from flask import Flask
from flask import request
from src.model.commands.java_command import JavaCommand
from src.model.commands.python_command import PythonCommand
from src.model.commands.nodejs_command import NodeJSCommand
from src.model.execute import Execute
from src.model.parameter import Parameter

app = Flask(__name__)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(ROOT_DIR, '../inputs/')
pathlib.Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)


@app.route('/', methods=['POST'])
def route():
    print('test')

    file_code = request.files['file']
    lang = request.form.get('lang')
    version = request.form.get('version')
    file_path = os.path.join(UPLOAD_DIR, file_code.filename)
    file_code.save(file_path)

    if lang == 'java':
        java_command = JavaCommand()
        execute = Execute()
        parameter = Parameter(file_path, UPLOAD_DIR)
        command = java_command.build(parameter)
        result = execute.run(command)
        return result
    if lang == 'python':
        python_command = PythonCommand()
        execute = Execute()
        parameter = Parameter(file_path, UPLOAD_DIR)
        command = python_command.build(parameter)
        result = execute.run(command)
        return result
    if lang == 'nodejs':
        nodejs_command = NodeJSCommand()
        execute = Execute()
        parameter = Parameter(file_path, UPLOAD_DIR)
        command = nodejs_command.build(parameter)
        result = execute.run(command)
        return result


if __name__ == '__main__':
    app.run()

