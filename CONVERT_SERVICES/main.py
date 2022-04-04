#
# @converter_pdf_to_word.py Copyright (c) 2022 Jalasoft.
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

from CONVERT_SERVICES.src.controller.apis.uploader import Uploader
from CONVERT_SERVICES.src.controller.apis.downloader import Downloader

UPLOAD_FOLDER = 'saved_files/'  # here is the file where the images will be downloaded

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api = Api(app)


@app.route('/upload', methods=['GET', 'POST'])
def save_file():
    file = Uploader(request, app.config['UPLOAD_FOLDER'])
    return file.upload()


@app.route('/download/<string:file_name>')
def download_file(file_name):
    file = Downloader(request, app.config['UPLOAD_FOLDER'], file_name)
    return file.donwload()


if __name__ == '__main__':
    app.run(debug=True)
