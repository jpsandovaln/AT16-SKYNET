import os
import pathlib
import json
from flask import Flask
from flask import request
from flask import Response
from http import HTTPStatus
from src.model.commands.java_command import JavaCommand
from src.model.commands.python_command import PythonCommand
from src.model.commands.nodejs_command import NodeJSCommand
from src.model.execute import Execute
from src.model.parameter import Parameter
from src.controller.result.success_result import SuccessResult
from src.controller.result.error_result import ErrorResult
from src.model.exceptions.compiler_exception import CompilerException

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

    try:
        parameter = Parameter(file_path, UPLOAD_DIR)

        if lang == 'java':
            java_command = JavaCommand()
            command = java_command.build(parameter)
        if lang == 'python':
            python_command = PythonCommand()
            command = python_command.build(parameter)

        execute = Execute()
        result = execute.run(command)
        result_compiler = SuccessResult(HTTPStatus.OK, str(result))
        return Response(
            json.dumps(result_compiler.__dict__),
            status=HTTPStatus.OK,
            mimetype='application/json'
        )
    except CompilerException as error:
        result_error = ErrorResult(error.status, error.message, error.code)
        return Response(
            json.dumps(result_error.__dict__),
            status=error.status,
            mimetype='application/json'
        )
    except Exception as error:
        result_error = ErrorResult(HTTPStatus.NOT_FOUND, error, 'AT16-000451')
        return Response(
            json.dumps(result_error.__dict__),
            status=HTTPStatus.NOT_FOUND,
            mimetype='application/json'
        )


if __name__ == '__main__':
    app.run()

