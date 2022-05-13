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

from src.common.exceptions.parameter_exception import ParameterException
from src.model.parameters import Parameters
import os


# Take request, the save location and the server url to upload files, downloads and get the request
class EndPointConverter:
    def __init__(self, request, save_location, server_url):
        self.request = request
        self.save_location = save_location
        self.server_url = server_url

    def upload(self):
        file = self.request.files['file']
        path_saved = os.path.join(self.save_location, file.filename)
        parameters = Parameters(path_saved, self.request)
        parameters.validate()
        parameters.validate_get_convert()
        file.save(path_saved)  # To save the file
        parameters.validate_file()
        parameters.validate_in_format()
        return 1

    def get_request(self):
        return self.request

    def send_file(self, dir_output, file_name):
        return self.server_url + os.path.join(dir_output, file_name)
