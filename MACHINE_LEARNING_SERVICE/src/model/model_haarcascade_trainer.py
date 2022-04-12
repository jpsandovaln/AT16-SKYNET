import cv2
import os

import numpy as np

data_Path = r'C:\Skynet\AT16-SKYNET\MACHINE_LEARNING_SERVICE\src\controller\utils\images_haarcascade'
people_List = os.listdir(data_Path)
print('lista de personas', people_List)

labels = []
faces_Data = []
label = 0

for nameDir in people_List:
    person_Path = data_Path + '/' + nameDir
    print('leyendo imagenes')

    for fileName in os.listdir(person_Path):
        print('Rostros: ', nameDir + '/' + fileName)
        labels.append(label)
        faces_Data.append(cv2.imread(person_Path + '/' + fileName, 0))
        img = cv2.imread(person_Path + '/' + fileName, 0)
    label = label + 1

face_recognizer = cv2.face.EigenFaceRecognizer_create()

print("Entrenando...")
face_recognizer.train(faces_Data, np.array(labels))

face_recognizer.write(r'C:\Skynet\AT16-SKYNET\MACHINE_LEARNING_SERVICE\src\model\trained_models\ModelTraining.xml')
print("Entrenamiento finalizado")