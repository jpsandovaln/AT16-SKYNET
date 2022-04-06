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

from src.model.convertimage import ConvertImage
from src.model.convertvideo import ConvertVideo
from flask import Flask
from flask_restful import Api
from flask import request
from src.controller.apis.endpointconverter import EndPointConverter


UPLOAD_FOLDER = r'saved_files/upload'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api = Api(app)


@app.route('/Convert', methods=['POST'])
def save_file():
    file = EndPointConverter(request, app.config['UPLOAD_FOLDER'])
    result = file.Upload()
    if result == 1:
        if request.values.get('Convert') == 'Image':
            prueba = ConvertImage(request, UPLOAD_FOLDER)
        if request.values.get('Convert') == 'Video':
            prueba = ConvertVideo(request, UPLOAD_FOLDER)
        prueba.Exec()
        return file.Send_File(prueba.output_file, prueba.name_output)


if __name__ == '__main__':
    app.run(debug=True)
