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


# Class para endpoint in Postman
class EndPointConverter:
    def __init__(self, request: any, save_location: str):
        self.request: any = request
        self.save_location: str = save_location

    # Upload files in folder of Machine Learning Saved Files
    def Upload(self) -> int:
        if self.request.method == 'POST':
            file: any = self.request.files['file']
            file.save(os.path.join(self.save_location, file.filename))
            return 1

    def getRequest(self) -> any:
        return self.request

    # Download files in folder of Machine Learning Saved Files
    def Send_File(self, dir_output: str, file_name: str) -> str:
        return ( r'http://127.0.0.1:5000/downloader/' + os.path.join(dir_output, file_name))
