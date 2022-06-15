#
# @zip.py Copyright (c) 2022 Jalasoft.
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

import zipfile
from decouple import config
from absolute_path import AbsolutePath
import os


absolute_path = AbsolutePath.get_absolute_path()
# This is the path where the zip file will be saved
path_img_zip = os.path.join(absolute_path, config('PATH_IMAGE'))


class UnzipFile:
    def __init__(self, path_saved):
        self.path_saved = str(path_saved)

    def decom_zip(self):
        path_zip = format(self.path_saved)
        file_zip = zipfile.ZipFile(path_zip)  # This is the input path
        file_zip.extractall(path_img_zip)  # This is the output path
