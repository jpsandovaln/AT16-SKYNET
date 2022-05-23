import cv2
import os

import numpy as np

data_Path: str = r'C:\Skynet\AT16-SKYNET\MACHINE_LEARNING_SERVICE\src\controller\utils\images_haarcascade'
people_List: list[str] = os.listdir(data_Path)
print('lista de personas', people_List)

labels: list[int] = []
faces_Data: list = []
label: int = 0

for nameDir in people_List:
    person_Path: str = data_Path + '/' + nameDir
    print('leyendo imagenes')

    for fileName in os.listdir(person_Path):
        print('Rostros: ', nameDir + '/' + fileName)
        labels.append(label)
        faces_Data.append(cv2.imread(person_Path + '/' + fileName, 0))
        img: None = cv2.imread(person_Path + '/' + fileName, 0)
    label: int = label + 1

face_recognizer: None = cv2.face.EigenFaceRecognizer_create()

print("Entrenando...")
face_recognizer.train(faces_Data, np.array(labels))

face_recognizer.write(r'C:\Skynet\AT16-SKYNET\MACHINE_LEARNING_SERVICE\src\model\trained_models\ModelTraining.xml')
print("Entrenamiento finalizado")