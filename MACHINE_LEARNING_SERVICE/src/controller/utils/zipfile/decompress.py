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

PATH: str = r'C:\Skynet\AT16-SKYNET\MACHINE_LEARNING_SERVICE'


# Unzip a compressed file.
class Decompress:

    def __init__(self, path_saved: any):
        self.path_saved = str(path_saved)

    # Unzip a compressed file.
    def dec_zip(self) -> str:
        zip_path: str = format(self.path_saved)
        fzip: zipfile.ZipFile = zipfile.ZipFile(zip_path)
        find_path_decompress: int = zip_path.find('compress_files')
        path_decompress_saved: str = zip_path[:find_path_decompress]+'decompress_files'
        fzip.extractall(path_decompress_saved)
        return path_decompress_saved

    # Returns the path of the uncompressed file.
    def path_decompress(self) -> str:
        path_decompress: str = self.dec_zip()
        file_name: int = self.path_saved.find('compress_files')
        return path_decompress+self.path_saved[file_name+14:-4]
