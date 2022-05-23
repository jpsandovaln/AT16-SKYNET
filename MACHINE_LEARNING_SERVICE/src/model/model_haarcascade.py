#
# @model_haarcascade.py Copyright (c) 2022 Jalasoft.
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

import cv2 as cv
import os

from cv2 import VideoCapture, CascadeClassifier


class ModelHaarcascade:
    def __init__(self, data_path: any, face_path: any):
        self.data_path: any = data_path
        self.face_path: any = face_path
        self.model_path: str = 'src\model\ModelTraining.xml'
        print('Nueva instancia creada')


    def face_recognizer(self, name: str, path: str) -> str:
        path2: str = r'' + path
        result_str: str = 'No se ha encontrado a ' + str(name)
        data_path: any = self.data_path
        image_paths: list[str] | list[bytes] = os.listdir(data_path)
        face_recognizer: None = cv.face.EigenFaceRecognizer_create()
        face_recognizer.read(self.model_path)
        cap: VideoCapture = cv.VideoCapture(0)
        face_classif: CascadeClassifier = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

        while True:
            ret, frame = cap.read()
            if ret == False: break
            gray: None = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            aux_Frame: any = gray.copy()
            faces: None = face_classif.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                rostro: any = aux_Frame[y:y + h, x:x + w]
                rostro: any = cv.resize(rostro, (150, 150), interpolation=cv.INTER_CUBIC)
                result: any = face_recognizer.predict(rostro)

                if image_paths[result[0]] == name:
                    cv.putText(frame, '{}'.format(image_paths[result[0]]), (x, y - 25), 2, 1.1, (0, 255, 0), 1, cv.LINE_AA)
                    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    result_str: str = 'Se ha encontrado a ' + name

                else:
                    cv.putText(frame, 'Desconocido', (x, y - 20), 2, 0.8, (0, 0, 255), 1, cv.LINE_AA)
                    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            cv.imshow('frame', frame)
            Key: None = cv.waitKey(1)
            if Key == 27 or result_str == 'Se ha encontrado a ' + name:
                break

        cap.release()
        cv.destroyAllWindows()
        return result_str


#model_prueba = ModelHaarcascade()
#print(model_prueba.face_recognizer('Albert', r'C:\Skynet\AT16-SKYNET\MACHINE_LEARNING_SERVICE\saved_files\save_recognizer_videos\video2.mp4'))