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

import os


class ControllerFaceRecognizer:
    def __init__(self, request: any, save_location: any):
        self.request: any = request
        self.save_location: any = save_location
        self.name_request: any = request.form.get('name')

    def save_file(self):
        file: any = self.request.files['file']
        file.save(os.path.join(self.save_location, file.filename))

    def get_path(self):
        if self.request.method == 'POST':
            file_request: any = self.request.files['file']
            file_request.save(os.path.join(self.save_location, file_request.filename))
            print(os.path.join(self.save_location, file_request.filename))
        return os.path.join(self.save_location, file_request.filename)

    def get_name(self):
        return self.name_request
