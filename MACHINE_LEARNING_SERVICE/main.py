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

import os
from flask import Flask
from flask_restful import Api
from flask import request
from flask import send_file
from src.controller.apis.controller_machine import ControllerMachineLearning
from src.controller.apis.downloader import Downloader
from src.controller.apis.controller_vggface import ControllerVggFace
from src.controller.apis.controller_iris_recognizer import ControllerIris
from src.controller.apis.controller_iris_train_model import ControllerIrisTrain
from src.model.model_haarcascade import ModelHaarcascade
from src.controller.apis.controller_face_recognizer import ControllerFaceRecognizer
#from src.model.face_emotion import FaceEmotion
#from src.controller.apis.endpointface import EndPointConverter
from decouple import config


#UPLOAD_FOLDER = config('UPLOAD_FOLDER')
#UPLOAD_FACE_FOLDER = config('UPLOAD_FACE_FOLDER')
#UPLOAD_VGGFACE = config('UPLOAD_VGGFACE')
#HAARCASCADE_IMAGES = config('HAARCASCADE_IMAGES')
#HAARCASCADE_XML = config('HAARCASCADE_XML')
#VGGFACE_COMPRESS = config('VGGFACE_COMPRESS')
#VGGFACE_DECOMPRESS = config('VGGFACE_DECOMPRESS')
#UPLOAD_IRIS = config('UPLOAD_IRIS')


# para docker
UPLOAD_FOLDER2 = r'/app/saved_files/compress_files'
UPLOAD_FACE_FOLDER2 = r'/app/saved_files/save_recognizer_videos'
UPLOAD_VGGFACE2 = r'/app/saved_files/vgg_files'
HAARCASCADE_IMAGES2 = r'/app/src/controller/utils/images_haarcascade'
HAARCASCADE_XML2 = r'/app/src/controller/utils/haarcascade_algorithms'
VGGFACE_COMPRESS2 = r'/app/saved_files/vggface_files/compress_files'
VGGFACE_DECOMPRESS2 = r'/app/saved_files/vggface_files/decompress_files'
UPLOAD_IRIS2 = r'/app/saved_files/save_iris_files'
UPLOAD_FOLDER = r'/app/saved_files/upload'

# # This is the path where the zip file will be saved
# UPLOAD_FOLDER2 = r'saved_files\compress_files'
# UPLOAD_FACE_FOLDER2 = r'saved_files\save_recognizer_videos'
# UPLOAD_VGGFACE2 = r'saved_files/vgg_files/'
# HAARCASCADE_IMAGES2 = r'src\controller\utils\images_haarcascade'
# HAARCASCADE_XML2 = r'src\controller\utils\haarcascade_algorithms'
# VGGFACE_COMPRESS2 = r'saved_files\vggface_files\compress_files'
# VGGFACE_DECOMPRESS2 = r'saved_files\vggface_files\decompress_files'
# UPLOAD_IRIS2 = r'saved_files\save_iris_files'
# UPLOAD_FOLDER = r'saved_files/upload'  # for emotion CAUTION

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER2
app.config['UPLOAD_FOLDER_EMOTION'] = UPLOAD_FOLDER
app.config['UPLOAD_FACE_FOLDER'] = UPLOAD_FACE_FOLDER2
app.config['UPLOAD_VGGFACE'] = UPLOAD_VGGFACE2
app.config['HAARCASCADE_IMAGES'] = HAARCASCADE_IMAGES2
app.config['HAARCASCADE_XML'] = HAARCASCADE_XML2
app.config['VGGFACE_COMPRESS'] = VGGFACE_COMPRESS2
app.config['VGGFACE_DECOMPRESS'] = VGGFACE_DECOMPRESS2
app.config['UPLOAD_IRIS'] = UPLOAD_IRIS2
api = Api(app)


# End point of the uploader file
@app.route('/object_recognizer', methods=['GET', 'POST'])
def save_file():
    file = ControllerMachineLearning(request, app.config['UPLOAD_FOLDER'])
    return file.upload()


@app.route('/face_recognizer', methods=['POST'])
def identify():
    file = ControllerFaceRecognizer(request, app.config['UPLOAD_FACE_FOLDER'])
    file.save_file()
    model = ModelHaarcascade(app.config['HAARCASCADE_IMAGES'], app.config['HAARCASCADE_XML'])
    return model.face_recognizer(file.get_name(), file.get_path())


# Endpoint for compare 1 persons in a folder with images
@app.route('/vggface_search_person', methods=['POST'])
def face_search():
    response = ControllerVggFace(request)
    return response.search_person(app.config['VGGFACE_COMPRESS'])


# Endpoint for recognize the emotions in an image
# @app.route('/emotion', methods=['POST'])
# def emotion_search():
#     file = EndPointConverter(request, app.config['UPLOAD_FOLDER_EMOTION'])
#     recognize = FaceEmotion(request, UPLOAD_FOLDER)
#     file.upload()
#     recognize.find_faces()
#     return file.send_file(UPLOAD_FOLDER, recognize.name)


# End point of the downloader file
@app.route('/download/<string:save>/<string:output_file>/<string:file_name>', methods=['GET'])
def download_file(save, output_file, file_name):
    return send_file(os.path.join(save, output_file, file_name), as_attachment=True)


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
