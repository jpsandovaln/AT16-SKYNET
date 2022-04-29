#
# @main.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# Edificio Union № 1376 Av. General Inofuentes esquina Calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
import json
from http import HTTPStatus
from src.model.convert_image import ConvertImage
from src.model.convert_video import ConvertVideo
from src.model.convert_metadata import ConvertMetadata
from src.model.convert_audio import ConvertAudio
from src.model.convert_ocr import ConvertOCR
from src.controller.apis.end_point_converter import EndPointConverter
from src.common.exceptions.convert_services_exception import ConvertServicesException
from src.controller.results.success_result import SuccessResult
from src.controller.results.error_result import ErrorResult
from flask import send_file
from flask import Flask
from flask_restful import Api
from flask import request
from flask import Response
import os


UPLOAD_FOLDER = r'saved_files\upload'  # here que common files are saved
DOWNLOADER_FOLDER = r'saved_files\{}'  # here que specific files are saved after convert
SEVER_URL_DOWNLOAD = r'http://127.0.0.1:5000/downloader/'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEVER_URL_DOWNLOAD'] = SEVER_URL_DOWNLOAD
api = Api(app)


# Download the files for all convertors
@app.route('/downloader/<string:save>/<string:output_file>/<string:file_name>', methods=['GET'])
def get_file(save, output_file, file_name):
    save_path = (os.path.join(save, output_file, file_name))
    return send_file(save_path, as_attachment=True)


# Save the file and send it to the different convertors depending on the "convert" param
@app.route('/convert', methods=['POST'])
def save_file():
    try:
        file = EndPointConverter(request, app.config['UPLOAD_FOLDER'],
                                 app.config['SEVER_URL_DOWNLOAD'])
        result = file.upload()
        if result == 1:
            if request.values.get('convert') == 'Image':
                convert = ConvertImage(request, UPLOAD_FOLDER)
            if request.values.get('convert') == 'Video':
                convert = ConvertVideo(request, UPLOAD_FOLDER)
            if request.values.get('convert') == 'Metadata':
                convert = ConvertMetadata(request, UPLOAD_FOLDER)
            if request.values.get('convert') == 'Audio':
                convert = ConvertAudio(request, UPLOAD_FOLDER)
            if request.values.get('convert') == 'OCR':
                convert = ConvertOCR(request, UPLOAD_FOLDER)
            convert.exec()
            result_converter = file.send_file(convert.output_file, convert.name_output)
            result_model = SuccessResult(HTTPStatus.OK, str(result_converter))
            return Response(
                json.dumps(result_model.__dict__),
                status=HTTPStatus.OK,
                mimetype='application/json'
            )
    except ConvertServicesException as error:
        result_error = ErrorResult(error.status, error.message,
                                   error.code)
        return Response(
            json.dumps(result_error.__dict__),
            status=error.status,
            mimetype='application/json'
        )
    except Exception as error:
        result_error = ErrorResult(HTTPStatus.NOT_FOUND, error,
                                   'AT16-000451')
        return Response(
            json.dumps(result_error.__dict__),
            status=HTTPStatus.NOT_FOUND,
            mimetype='application/json'
        )


if __name__ == '__main__':
    app.run(debug=True)
