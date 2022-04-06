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

import os
from flask import send_file


class EndPointConverter:
    def __init__(self, request, save_location):
        self.request = request
        self.save_location = save_location

    def Upload(self):
        if self.request.method == 'POST':
            file = self.request.files['file']
            file.save(os.path.join(self.save_location, file.filename))
            return 1

    def getRequest(self):
        return self.request

    def Send_File(self, dir_output, file_name):
        return send_file( os.path.join(dir_output, file_name) )