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

from CONVERT_SERVICES.src.converter.controller.rest_api_dayler.resources.file_downloader import FileDownloader
from CONVERT_SERVICES.src.converter.controller.rest_api_dayler.resources.file_uploader import FileUploader

app = Flask(__name__)
api = Api(app)


api.add_resource(FileUploader, '/files')
api.add_resource(FileDownloader, '/file/<string:file_id>')

if __name__ == '__main__':
    app.run(debug=True)
