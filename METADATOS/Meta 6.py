#
# @video_converter.py Copyright (c) 2022 Jalasoft
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

### DEFINIMOS LAS ENTRADAS DE LA CLASE
    def __init__(self,meti):
        self.path = "C:/IVAN/CODING/Metadatos/filein"
        self.direct = "C:/IVAN/CODING/Metadatos/metaout/"
        self.meti = meti

### definimosla funcion
    def select_file(self):
        direc = os.listdir(self.path)## sacamos el nombre de cada archivo de la carpeta
        exe = "Exiftool"##inicializamos el ejecutable como constante
        for file in direc:
            if os.path.isfile(os.path.join(self.path,file)):
                name = str(file)
                namef=name.split('.')
#                namef = name[:-5]## eliminamos la extencion del archivo en el caso del ejemplo el
                # ".jpg"
                if self.meti == 'json':
                ##procesamos cada archivo con el Exiftool.exe y sacamos sus dependencias en
                # formato JSON creando un archivo.JSON para cada imagen
                    process = subprocess.run([exe,str(self.path) + "/" + str(file), '-' + str(
                        self.meti), '-W+!', str(self.direct) + namef[0] + '.' + str(self.meti)])
                ## imprimimos el estado de cada conversion
                    print(process.stdout)
                ###--******************************************************************************
                elif self.meti == 'txt':
                    process = subprocess.run([exe, str(self.path) + "/" + str(file), '-W+!',
                                              str(self.direct) + namef[0] + '.' + str(self.meti)])
                    ## imprimimos el estado de cada conversion
                    print(process.stdout)
                ##-********************************************************************************
                else : ## si es XMP
                    process = subprocess.run([exe, str(self.path) + "/" + str(file), '-o',
                                               str(self.direct) + namef[0] + '.' + str(self.meti)])
                    ## imprimimos el estado de cada conversion
                    print(process.stdout)


######### LLAMAMOS A NUESTRA CLASE CON LOS VALORES DE LA DIRECCION DE ENTRADA, LA EXTENCION Y LA
# SALIDA
prueba = Metadata('xmp')
prueba.select_file()