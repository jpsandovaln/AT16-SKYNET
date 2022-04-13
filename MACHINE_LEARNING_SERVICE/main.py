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

from mtcnn.mtcnn import MTCNN
import matplotlib.pyplot as pyplot
from PIL import Image
import numpy as np
from flask import send_file
import os
from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input
from src.model.model_vggface import ModelVggFace


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

@app.route('/vggface', methods=['POST'])
def face():
    imagen = request.files['file']
    img = pyplot.imread(imagen)
    detector = MTCNN()
    results = detector.detect_faces(img)

    x1, y1, width, height = results[0]['box']
    x2, y2 = x1 + width, y1 + height
    face = img[y1:y2, x1:x2]
    image = Image.fromarray(face)
    image = image.resize((224,224))
    face_array = np.asarray(image)
    im = Image.fromarray(face_array)
    im.save(os.path.join('saved_files', imagen.filename))
    return send_file(os.path.join('saved_files', imagen.filename))


@app.route('/vggface2', methods=['POST'])
def facerecog(filenames):
    faces = ['saved_files/persona1.jpg' for f in filenames]
    samples = np.asarray(faces, 'float32')
    samples = preprocess_input(samples, version=2)
    model = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3), pooling='avg')
    yhat = model.predict(samples)
    return yhat


@app.route('/vggface3', methods=['POST'])
def facerecog2():
    #filenames = ['C:/Users/Jhon/Pictures/faces/sharon_stone1.jpg', 'C:/Users/Jhon/Pictures/faces/persona3.jpg', 'C:/Users/Jhon/Pictures/faces/channing_tatum.jpg']
    filenames = ['C:/Users/Jhon/Pictures/faces/will_smith.jpg',
                 'C:/Users/Jhon/Pictures/faces/w.jpg',
                 'C:/Users/Jhon/Pictures/faces/sharon_stone1.jpg']

    model = ModelVggFace()
    embeddings = model.get_embeddings(filenames)
    return 'son la misma persona? ' + model.is_match(embeddings[0], embeddings[0])
    #print('Positive Test')
    #model.is_match(embeddings[0], embeddings[1])
    #print('Negative Tests')
    #model.is_match(embeddings[0], embeddings[2])


@app.route('/vggface4', methods=['POST'])
def facerecog3():
    img1 = request.files['person1']
    img2 = request.files['person2']
    #filenames = ['C:/Users/Jhon/Pictures/faces/sharon_stone1.jpg', 'C:/Users/Jhon/Pictures/faces/persona3.jpg', 'C:/Users/Jhon/Pictures/faces/channing_tatum.jpg']
    filenames = [img1, img2]
    model = ModelVggFace()
    embeddings = model.get_embeddings(filenames)
    return 'Are they the same person? ' + model.is_match(embeddings[0], embeddings[1])


# Starts the API, maintains the debugger active, don't use it in a production
# deployment
if __name__ == '__main__':
    app.run(debug=True)
