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
    def __init__(self,path,ext,direct):
        self.path=path
        self.ext=ext
        self.direct=direct
### definimosla funcion
    def select_file(self):
        direc= os.listdir(self.path)## sacamos el nombre de cada archivo de la carpeta
        exe = "Exiftool"##inicializamos el ejecutable como constante
        for file in direc:
            if os.path.isfile(os.path.join(self.path,file)) and file.endswith(
                    self.ext):##limitamos el tipo de archivo que entrara con la extencion ".jpg"
                ##procesamos cada archivo con el Exiftool.exe y sacamos sus dependencias en
                # formato JSON creando un archivo.JSON para cada imagen
                process = subprocess.run([exe,str(self.path) + "/" + str(file), '-json', '-W+!',
                                            str(self.direct)+ str(file) + ".json"])
                ## imprimimos el estado de cada conversion
                print(process.stdout)
######### LLAMAMOS A NUESTRA CLASE CON LOS VALORES DE LA DIRECCION DE ENTRADA, LA EXTENCION Y LA
# SALIDA
prueba = Metadata("C:/IVAN/CODING/Metadatos/imagenes",'.jpg',"C:/IVAN/CODING/Metadatos/metaout/")
prueba.select_file()