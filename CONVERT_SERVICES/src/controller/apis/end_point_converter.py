# 
# @end_point_converter.py Copyright (c)
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


class EndPointConverter:
    def __init__(self, request, save_location):
        self.request = request
        self.save_location = save_location

    def upload(self):
        file = self.request.files['file']
        file.save(os.path.join(self.save_location, file.filename))
        return 1

    def get_request(self):
        return self.request

    def send_file(self, dir_output, file_name):
        return r'http://127.0.0.1:5000/downloader/' + os.path.join(dir_output, file_name)
