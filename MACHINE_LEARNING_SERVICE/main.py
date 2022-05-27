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
from src.controller.apis.controller_vggface import ControllerVggFace
from src.controller.apis.controller_iris_recognizer import ControllerIris
from src.controller.apis.controller_iris_train_model import ControllerIrisTrain
from decouple import config
from absolute_path import AbsolutePath
import os
from src.model.face_emotion import FaceEmotion
from flask import send_file
from src.controller.apis.endpointface import EndPointConverter


absolute_path = AbsolutePath.get_absolute_path()
# This is the path where the zip file will be saved
UPLOAD_FOLDER = os.path.join(absolute_path, config('UPLOAD_FOLDER'))
UPLOAD_FACE_FOLDER = os.path.join(absolute_path, config('UPLOAD_FACE_FOLDER'))
UPLOAD_VGGFACE = os.path.join(absolute_path, config('UPLOAD_VGGFACE'))
HAARCASCADE_IMAGES = os.path.join(absolute_path, config('HAARCASCADE_IMAGES'))
HAARCASCADE_XML = os.path.join(absolute_path, config('HAARCASCADE_XML'))
VGGFACE_COMPRESS = os.path.join(absolute_path, config('VGGFACE_COMPRESS'))
VGGFACE_DECOMPRESS = os.path.join(absolute_path, config('VGGFACE_DECOMPRESS'))
UPLOAD_IRIS = os.path.join(absolute_path, config('UPLOAD_IRIS'))

UPLOAD_FOLDER_EMOTIONS = r'saved_files/upload'
DOWNLOADER_FOLDER = r'saved_files/{}'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FACE_FOLDER'] = UPLOAD_FACE_FOLDER
app.config['UPLOAD_VGGFACE'] = UPLOAD_VGGFACE
app.config['HAARCASCADE_IMAGES'] = HAARCASCADE_IMAGES
app.config['HAARCASCADE_XML'] = HAARCASCADE_XML
app.config['VGGFACE_COMPRESS'] = VGGFACE_COMPRESS
app.config['VGGFACE_DECOMPRESS'] = VGGFACE_DECOMPRESS
app.config['UPLOAD_IRIS'] = UPLOAD_IRIS
api = Api(app)


@app.route('/downloader/<string:save>/<string:output_file>/<string:file_name>', methods=['GET'])
def get_file(save, output_file, file_name):
    x = (os.path.join(output_file, file_name))
    y = (os.path.join(save, x))
    return send_file(y, as_attachment=True)


@app.route('/Emotion', methods=['POST'])
def save_file_emotion():
    file = EndPointConverter(request, app.config['UPLOAD_FOLDER'])
    prueba = FaceEmotion(request, UPLOAD_FOLDER)
    result = file.Upload()
    image_new = prueba.find_faces()
    return file.Send_File(UPLOAD_FOLDER_EMOTIONS, prueba.name)


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
    file.save_file()
    model = ModelHaarcascade(app.config['HAARCASCADE_IMAGES'], app.config['HAARCASCADE_XML'])
    return model.face_recognizer(file.get_name(), file.get_path())


# Endpoint for crop a face in an image
@app.route('/vggface_crop', methods=['POST'])
def crop_face():
    face = ControllerVggFace(request)
    return face.crop_face(app.config['VGGFACE_DECOMPRESS'])


# Endpoint for compare 2 persons in 2 images
@app.route('/vggface_compare', methods=['POST'])
def face_compare():
    response = ControllerVggFace(request)
    return response.compare_faces()


# Endpoint for compare 1 persons in a folder with images
@app.route('/vggface_search_person', methods=['POST'])
def face_search():
    response = ControllerVggFace(request)
    return response.search_person(app.config['VGGFACE_COMPRESS'])


@app.route('/iris_recognition', methods=['POST'])
def iris_recognition():
    file = ControllerIris(request, app.config['UPLOAD_IRIS'])
    return file.upload()


@app.route('/iris_recognition_train', methods=['POST'])
def train_iris():
    file = ControllerIrisTrain(request, app.config['UPLOAD_IRIS'])
    return file.upload()


# Starts the API, maintains the debugger active, don't use it in a production
# deployment
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
