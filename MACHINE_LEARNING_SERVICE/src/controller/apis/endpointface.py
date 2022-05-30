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
from decouple import config


URL = config('URL')


# Class para endpoint in Postman
class EndPointConverter:
    def __init__(self, request, save_location):
        self.request = request
        self.save_location = save_location

    # Upload files in folder of Machine Learning Saved Files
    def upload(self):
        if self.request.method == 'POST':
            file = self.request.files['file']
            file.save(os.path.join(self.save_location, file.filename))
            return 1

    def get_request(self):
        return self.request

    # Download files in folder of Machine Learning Saved Files
    def send_file(self, dir_output, file_name):
        return URL + os.path.join(dir_output, file_name)
