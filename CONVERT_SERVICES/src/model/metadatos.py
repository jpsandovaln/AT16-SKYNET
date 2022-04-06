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


# CREAMOS NUESTRA CLASE

class Metadata:

# define the input of class
    def __init__(self, meta, dir):
        self.path = "..//..//saved_files/metadata_upload" ## carpeta de entrada
        self.file = dir
        self.direct = "..//..//saved_files/metadata_download"## carpeta de salida
        self.meti = meta

### define function for extract metadatos
    def Select_File(self):
#       direc = os.listdir(self.path)## charge the name of all files in folder
        exe = "..//..//third_party/win/Exiftool"## rename executable
#        for file in direc:
#            if os.path.isfile(os.path.join(self.path,file)):
        name = str(self.file)
        namef = name.split('.')

        ##Process all files with exiftools.exe and extract Metadatos

        if self.meti == 'json':
            process = subprocess.run([exe, str(self.path) + "/" + str(self.file), '-' +
                                      str(self.meti), '-W+!', str(self.direct) + "/" + namef[0] +
                                      '.' + str(self.meti)])
        elif self.meti == 'txt':
            process = subprocess.run([exe, str(self.path) + "/" + str(self.file), '-W+!',
                                      str(self.direct) + "/" + namef[0] + '.' + str(self.meti)])
        else:
            process = subprocess.run([exe, str(self.path) + "/" + str(self.file), '-O',
                                      str(self.direct) + "/" + namef[0] + '.' + str(self.meti)])
        print(process.stdout)

#(exe,entrada path,-jason,-W+!,salidapath/name.json)
#(exe,entrada path,-W+!,salidapath/name.txt)
#(exe, entradapath,-o,salidapath/name.xmp)
# cambio de pull request
# Call the object and run the function with 1 parameter, it is the extencion of output


prueba = Metadata('xmp', "BugAdvocacy2008.pdf")
prueba.Select_File()