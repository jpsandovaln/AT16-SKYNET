#
# @main.py Copyright (c) 2022 Jalasoft.
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


class Classroom:

    def decom_zip(self, filename):
        path_zip = '../../../../../compress_file/{}'.format(filename)
        fzip = zipfile.ZipFile(path_zip)  # This is the input path
        fzip.extractall("../../../../saved_files")  # This is the output path
        print('Ya está')
