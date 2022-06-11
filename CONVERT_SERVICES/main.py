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
from src.model.convert_translator import ConvertTranslator
from src.model.convert_wav_to_txt import ConvertWavTxt
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
from flask_cors import CORS


# modified path to work with linux in a docker container
UPLOAD_FOLDER: str = r'saved_files/upload'  # here que common files are saved
DOWNLOADER_FOLDER: str = r'saved_files/{}'  # here que specific files are saved after convert
SEVER_URL_DOWNLOAD: str = r'http://127.0.0.1:6008/downloader/'

app: Flask = Flask(__name__)
cors = CORS(app)
app.config['UPLOAD_FOLDER']: str = UPLOAD_FOLDER
app.config['SEVER_URL_DOWNLOAD']: str = SEVER_URL_DOWNLOAD
api: Api = Api(app)


# Download the files for all convertors
@app.route('/downloader/<string:save>/<string:output_file>/<string:file_name>', methods=['GET'])
def get_file(save: any, output_file: any, file_name: any) -> str:
    save_path: str = (os.path.join(save, output_file, file_name))
    return send_file(save_path, as_attachment=True)


# Saves the file and send it to the different convertors depending on the "convert" param
@app.route('/convert', methods=['POST'])
def save_file():
    try:
        file: EndPointConverter = EndPointConverter(request, app.config['UPLOAD_FOLDER'],
                                                    app.config['SEVER_URL_DOWNLOAD'])
        result: int = file.upload()
        if result == 1:
            if request.values.get('convert') == 'Image':
                convert: ConvertImage = ConvertImage(request, UPLOAD_FOLDER)
            if request.values.get('convert') == 'Video':
                convert: ConvertVideo = ConvertVideo(request, UPLOAD_FOLDER)
            if request.values.get('convert') == 'Metadata':
                convert: ConvertMetadata = ConvertMetadata(request, UPLOAD_FOLDER)
            if request.values.get('convert') == 'Audio':
                convert: ConvertAudio = ConvertAudio(request, UPLOAD_FOLDER)
            if request.values.get('convert') == 'OCR':
                convert: ConvertOCR = ConvertOCR(request, UPLOAD_FOLDER)
            if request.values.get('convert') == 'Translator':
                convert: ConvertTranslator = ConvertTranslator(request, UPLOAD_FOLDER)
            if request.values.get('convert') == 'WavTxt':
                convert: ConvertWavTxt = ConvertWavTxt(request, UPLOAD_FOLDER)
            convert.exec()
            result_converter: any = file.send_file(convert.output_file, convert.name_output)
            result_model: SuccessResult = SuccessResult(HTTPStatus.OK, str(result_converter))
            return Response(
                json.dumps(result_model.__dict__),
                status=HTTPStatus.OK,
                mimetype='application/json'
            )
    except ConvertServicesException as error:
        result_error: ErrorResult = ErrorResult(error.status, error.message, error.code)
        return Response(
            json.dumps(result_error.__dict__),
            status=error.status,
            mimetype='application/json'
        )
    except Exception as error:
        result_error: ErrorResult = ErrorResult(HTTPStatus.NOT_FOUND, error, 'AT16-000451')
        return Response(
            json.dumps(result_error.__dict__),
            status=HTTPStatus.NOT_FOUND,
            mimetype='application/json'
        )


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5003)
