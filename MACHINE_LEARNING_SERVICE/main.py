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

from flask import Flask
from flask_restful import Api
from flask import request


from src.model.model_haarcascade import ModelHaarcascade
from src.controller.apis.controller_face_recognizer import ControllerFaceRecognizer
from src.controller.apis.controller_machine import ControllerMachineLearning
from src.controller.apis.downloader import Downloader

# This is the path where the zip file will be saved
UPLOAD_FOLDER = 'saved_files\compress_files'
UPLOAD_FACE_FOLDER = 'saved_files\save_recognizer_videos'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FACE_FOLDER'] = UPLOAD_FACE_FOLDER
api = Api(app)


# End point of the uploader file
@app.route('/object_recognizer', methods=['GET', 'POST'])
def save_file():
    file = ControllerMachineLearning(request, app.config['UPLOAD_FOLDER'])
    return file.upload()


# End point of the downloader file
@app.route('/download/<string:file_name>')
def download_file(file_name):
    file = Downloader(request, app.config['UPLOAD_FOLDER'], file_name)
    return file.download()


@app.route('/face_recognizer', methods=['POST'])
def identify():
    file = ControllerFaceRecognizer(request, app.config['UPLOAD_FACE_FOLDER'])
    print(file.get_path())
    model = ModelHaarcascade()
    return model.face_recognizer(file.get_name(), file.get_path())

# Starts the API, maintains the debugger active, don't use it in a production
# deployment
if __name__ == '__main__':
    app.run(debug=True)
