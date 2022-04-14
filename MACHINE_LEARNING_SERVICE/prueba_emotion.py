# 
# @object_result.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
# 
# This software is the confidential and proprietary information of
# Jalasoft, ("Condidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from MACHINE_LEARNING_SERVICE.src.model.face_emotion import Face_Emotion
from flask import send_file
from flask import Flask
from flask_restful import Api
from flask import request
import os
from MACHINE_LEARNING_SERVICE.src.controller.apis.endpointface import EndPointConverter


UPLOAD_FOLDER = r'saved_files/upload'
DOWNLOADER_FOLDER = r'saved_files\{}'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api = Api(app)

@app.route('/downloader/<string:save>/<string:output_file>/<string:file_name>', methods=['GET'])
def get_file(save, output_file, file_name):
    x = (os.path.join(output_file, file_name))
    y = (os.path.join(save, x))
    return send_file(y, as_attachment=True)

@app.route('/Emotion', methods=['POST'])
def save_file():
    file = EndPointConverter(request, app.config['UPLOAD_FOLDER'])
    prueba = Face_Emotion(request, UPLOAD_FOLDER)
    result = file.Upload()
    image_new = prueba.modify_image()

    return file.Send_File(UPLOAD_FOLDER, prueba.name)


if __name__ == '__main__':
    app.run(debug=True)