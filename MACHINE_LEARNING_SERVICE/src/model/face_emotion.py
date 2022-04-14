# 
# @object_result.py Copyright (c)
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


from keras.models import load_model
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
classifier = load_model('./Emotion_Detection.h5')

class_labels = ['Enojado', 'Feliz', 'Neutral', 'Triste', 'Sorprendido']

class Face_Emotion:
    def __init__(self, instructions, folder):
        self.name = instructions.files['file'].filename
        self.input_file = folder+'/' + self.name
        self.output_file = folder

    def find_emotion(self, image):
        preds = classifier.predict(image)[0]
        label = class_labels[preds.argmax()]
        return label

    def verify_images(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)
                label = self.find_emotion(roi)
                cv2.putText(image, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
                cv2.imwrite(self.output_file+'/'+self.name, image)
            else:
                label = 'no face found'
                cv2.putText(image, label, (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
                cv2.imwrite(self.name, image)
        return label

    def modify_image(self):
        dir = self.input_file
        image = cv2.imread(dir)
        label = self.verify_images(image)
        print (label)
        return 1





