#
# @filters_subject_state.py Copyright (c)
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

from flask import Flask
from flask_restful import Api

from rest_api.resources.downloader import FileDownloader
from rest_api.resources.uploader import FileUploader

app = Flask(__name__)
api = Api(app)


api.add_resource(FileUploader, '/files')
api.add_resource(FileDownloader, '/file/<string:file_id>')

if __name__ == '__main__':
    app.run(debug=True)
