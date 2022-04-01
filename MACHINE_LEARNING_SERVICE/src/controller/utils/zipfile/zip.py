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

# creation of compressed files
with zipfile.ZipFile("comprimidos.zip", "w") as fzip:
    fzip.write("calzip.txt")
    print("Archivos comprimidos")
#list zip file content
fzip = zipfile.ZipFile("comprimidos.zip")
print(fzip.printdir())
listaArchivos = fzip.namelist()
print(listaArchivos)
#We get more information
info = fzip.infolist()
for archivo in info:
        print(archivo.filename.archivo.date_time,archivo.compress_size)
        #descomprimir fichero
        fzip.extractall()#(ruta del archivo)
