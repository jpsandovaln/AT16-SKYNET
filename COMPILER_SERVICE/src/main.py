import os
import json
from flask import Flask
from flask import request
from flask import Response
from http import HTTPStatus
from dotenv import load_dotenv
from src.controller.result.success_result import SuccessResult
from src.controller.result.error_result import ErrorResult
from src.common.exceptions.compiler_exception import CompilerException
from src.controller.services.file_service import FileService
from src.common.exceptions.file_exception import FileException
from src.model.compiler_facade import CompilerFacade
from src.controller.properties.properties import Properties

app = Flask(__name__)
load_dotenv()
upload_dir = os.getenv('UPLOAD_DIR')


@app.route('/', methods=['POST'])
def route():
    lang = request.form.get('lang')
    version = request.form.get('version')

    try:
        file_path = FileService.get_file_path(request.files['file'], upload_dir)
        result = CompilerFacade.compiler_code(lang, file_path, upload_dir, Properties.get_binary_path(lang, version))
        result_compiler = SuccessResult(HTTPStatus.OK, str(result))
        return Response(
            json.dumps(result_compiler.__dict__),
            status=HTTPStatus.OK,
            mimetype='application/json'
        )
    except FileException as error:
        result_error = ErrorResult(error.status, error.message, 'AT16-CONT-12')
        return Response(
            json.dumps(result_error.__dict__),
            status=error.status,
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

