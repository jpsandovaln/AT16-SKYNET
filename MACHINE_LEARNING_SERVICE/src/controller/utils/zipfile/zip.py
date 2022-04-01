import zipfile

# creacion archivo comprimido
with zipfile.ZipFile("comprimidos.zip", "w") as fzip:
    fzip.write("calzip.txt")
    print("Archivos comprimidos")
#listar contenido del archivo zip
fzip = zipfile.ZipFile("comprimidos.zip")
print(fzip.printdir())
listaArchivos = fzip.namelist()
print(listaArchivos)
#obtenemos mas informacion
info = fzip.infolist()
for archivo in info:
        print(archivo.filename.archivo.date_time,archivo.compress_size)
        #descomprimir fichero
        fzip.extractall()#(ruta del archivo)
