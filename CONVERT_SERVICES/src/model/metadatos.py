#
# @metadato.py Copyright (c) 2022 Jalasoft
# 2643 Av Melchor Perez de Olguin , Colquiri Sud, Cochabamba, Bolivia.
# add direccion de jala la paz>
# All rights reserved
#
# This software is the confidential and proprietary information of
# Jalasoft , Confidential Information "). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft

import subprocess
import os

##CREAMOS NUESTRA CLASE
class Metadata:

### define the input of class
    def __init__(self,meti):
        self.path = "..//filein"
        self.direct = "..//metadata_output"
        self.meti = meti

### define function
    def select_file(self):
        direc = os.listdir(self.path)## charge the name of all files in folder
        exe = "..//..//third_party/win/Exiftool"## rename executable
        for file in direc:
            if os.path.isfile(os.path.join(self.path,file)):
                name = str(file)
                namef=name.split('.')

                ##Process all files with exiftools.exe and extract Metadatos

                if self.meti == 'json':
                    process = subprocess.run([exe,str(self.path) + "/" + str(file), '-' +
                            str(self.meti), '-W+!', str(self.direct) + "/" + namef[0] + '.' +
                                              str(self.meti)])
                elif self.meti == 'txt':
                    process = subprocess.run([exe, str(self.path) + "/" + str(file), '-W+!',
                            str(self.direct) + "/" + namef[0] + '.' + str(self.meti)])
                else:
                    process = subprocess.run([exe, str(self.path) + "/" + str(file), '-O',
                                    str(self.direct) + "/" + namef[0] + '.' + str(self.meti)])
                print(process.stdout)


##### Call the object and run the function with 1 parameter, it is the extencion of output

prueba = Metadata('txt')
prueba.select_file()