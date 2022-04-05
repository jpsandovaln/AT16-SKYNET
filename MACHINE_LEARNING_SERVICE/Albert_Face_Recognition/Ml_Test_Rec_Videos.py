import cv2
import os
import imutils

person_Name = 'Albert'
data_Path = 'D:/practicas de python/MLPrueba/data'
person_Path = data_Path + '/' + person_Name

if not os.path.exists(person_Path):
    print('Carpeta creada: ',person_Path)
    os.makedirs(person_Path)

#cap = cv2.VideoCapture('Documental_Big_Data.mp4')
cap = cv2.VideoCapture(0)
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0

while True:
    ret, frame = cap.read()
    if ret == False: break
    frame = imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aux_Frame = frame.copy()
    faces = faceClassif.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        rostro = aux_Frame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(person_Path + '/rostro_{}.jpg'.format(count), rostro)
        count =count +1
    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k == 27 or count >= 1000:
        break
