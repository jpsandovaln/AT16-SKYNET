# 
# @face_emotion.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
# 
# This software is the confidential and proprietary information of
# Jalasoft, ("Condidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
from operator import __add__
from tkinter import Image

from cv2 import CascadeClassifier
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np


CLASS_LABELS: list[str] = ['Enojado', 'Feliz', 'Neutral', 'Triste', 'Sorprendido']
GRAY: int = 0
COLOR: int = 2
SIZE_X: int = 48
SIZE_Y: int = 48
COLOR_RECTANGLE: tuple[int, int, int] = (255, 0, 0)
RECTANGLE_FACE: tuple[int, int, int] = (0, 255, 0)
CONST_DIV: float = 255.0
DATA_TYPE: str = 'float'
SIZE_FONT: int = 1
SCALE_FACTOR: float = 1.3
MIN_NEIGHBOURS: int = 5

face_classifier: CascadeClassifier = cv2.CascadeClassifier(r'src\model\haarcascade_frontalface_default.xml')
classifier: any | None = load_model(r'src\model\Emotion_Detection.h5')


# This method is static because all objects of kind FaceEmotion use this method for recognize emotion in a face
def find_emotion(image: Image) -> str | list[str]:
    predict: any = classifier.predict(image)[0]
    label: str | list[str] = CLASS_LABELS[predict.argmax()]
    return label


# This class is for recognize emotions
class FaceEmotion:

    # This construct is for recognize always need a file
    def __init__(self, instructions: str, folder: {__add__}):
        self.name: str = instructions.files['file'].filename
        self.input_file: str = folder+'/' + self.name
        self.output_file: any = folder

    # This method verify the faces has any emotion and this can be recognize for the model
    def verify_faces(self, image: Image, faces: any, gray: any) -> str:
        # x = pos X , y = pos Y , w = weight , h = height
        label: str = ''
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), COLOR_RECTANGLE, COLOR)
            img_gray: any = gray[y:y + h, x:x + w]
            img_gray: any = cv2.resize(img_gray, (SIZE_X, SIZE_Y), interpolation=cv2.INTER_AREA)
            if np.sum([img_gray]) != GRAY:
                img: float = img_gray.astype(DATA_TYPE) / CONST_DIV
                img: float = img_to_array(img)
                img: float = np.expand_dims(img, axis=GRAY)
                label: str = find_emotion(img)
            else:
                label: str = 'no face find'
            cv2.putText(image, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, SIZE_FONT, RECTANGLE_FACE, COLOR)
            cv2.imwrite(self.output_file + '/' + self.name, image)
        return label

    # This method find the faces in an image
    def find_faces(self):
        image: None = cv2.imread(self.input_file)
        gray: None = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces: None = face_classifier.detectMultiScale(gray, SCALE_FACTOR, MIN_NEIGHBOURS)
        label: str = self.verify_faces(image, faces, gray)
