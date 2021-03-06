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


# Unzip a compressed file.
class Decompress:

    def __init__(self, path_saved):
        self.path_saved = str(path_saved)

    # Unzip a compressed file.
    def dec_zip(self):
        zip_path = format(self.path_saved)
        fzip = zipfile.ZipFile(zip_path)
        find_path_decompress = zip_path.find('compress_files')
        path_decompress_saved = zip_path[:find_path_decompress]+'decompress_files'
        fzip.extractall(path_decompress_saved)
        return path_decompress_saved

    # Returns the path of the uncompressed file.
    def path_decompress(self):
        path_decompress = self.dec_zip()
        file_name = self.path_saved.find('compress_files')
        return path_decompress+self.path_saved[file_name+14:-4]
