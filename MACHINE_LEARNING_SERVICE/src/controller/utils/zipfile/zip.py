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

path_img_zip = 'src/controller/utils/images_iris_recognition'


class UnzipFile:
    def __init__(self, path_saved):
        self.path_saved = str(path_saved)

    def decom_zip(self):
        path_zip = format(self.path_saved)
        file_zip = zipfile.ZipFile(path_zip)  # This is the input path
        file_zip.extractall(path_img_zip)  # This is the output path

