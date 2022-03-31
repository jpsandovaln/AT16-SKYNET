#
# @downloader.py Copyright (c) 2022 Jalasoft.
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

from flask import send_file
import os


class Downloader:
    def __init__(self, request, source_folder, file_name):
        self.request = request
        self.source_folder = source_folder
        self.file_name = file_name

    def donwload(self):
        return send_file(os.path.join(self.source_folder, self.file_name), as_attachment=True)
