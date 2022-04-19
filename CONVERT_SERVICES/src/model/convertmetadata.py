#
# @convertmetadata.py Copyright (c) 2022 Jalasoft
# 2643 Av Melchor Perez de Olguin , Colquiri Sud, Cochabamba, Bolivia.
# add direccion de jala la paz>
# All rights reserved
#
# This software is the confidential and proprietary information of
# Jalasoft , ("Confidential Information "). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft

import subprocess
from src.model.convertor import Convertor


# Create a Class

class ConvertMetadata(Convertor):

    # define the input of class
    def __init__(self, input_data, input_file):
        super().__init__(input_data, input_file)
        self.path = input_file ## carpeta de entrada
        self.file = input_data.files['file'].filename

    # define function for extract metadata
    def exec(self):

        exe = "third_party/win/Exiftool"

        # Process all files with exiftools.exe and extract Metadatos
        if self.format == 'json':
            process = subprocess.run([exe, str(self.path) + "/" + str(self.file), '-' +
                                      str(self.format), '-W+!', str(self.output_file) + "/" +
                                      self.name_output])
        elif self.format == 'txt':
            process = subprocess.run([exe, str(self.path) + "/" + str(self.file), '-W+!',
                                      str(self.output_file) + "/" + self.name_output])
        else:
            process = subprocess.run([exe, str(self.path) + "/" + str(self.file), '-O',
                                      str(self.output_file) + "/" + self.name_output])
