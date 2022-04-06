#
# @controller_face_recognizer.py Copyright (c) 2022 Jalasoft.
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
from flask import request
from src.model.Result.model_result import ModelResult
from src.controller.utils.zipfile.decompress import \
    Decompress
import os

class ControllerFaceRecognizer:
    def __init__(self, request, save_location):
        self.request = request
        self.save_location = save_location
        self.name_request = request.form.get('name')

    def get_path(self):
        if self.request.method == 'POST':
            file_request = self.request.files['file']
            #self.name_request = request.form.get('name')
            file_request.save(os.path.join(self.save_location, file_request.filename))
            print(os.path.join(self.save_location, file_request.filename))
        return os.path.join(self.save_location, file_request.filename)

    def get_name(self):
        return self.name_request


#fl.save(os.path.join(self.save_location, fl.filename))


