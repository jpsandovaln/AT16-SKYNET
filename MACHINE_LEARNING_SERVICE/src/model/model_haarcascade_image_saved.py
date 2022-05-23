import cv2
import os
import imutils
from cv2 import VideoCapture, CascadeClassifier

person_Name: str = 'Albert'
data_Path: str = r'C:\Skynet\AT16-SKYNET\MACHINE_LEARNING_SERVICE\src\controller\utils\images_haarcascade'
person_Path: str = data_Path + '/' + person_Name

if not os.path.exists(person_Path):
    print('Carpeta creada: ', person_Path)
    os.makedirs(person_Path)

#cap = cv2.VideoCapture('Documental_Big_Data.mp4')
cap: VideoCapture = cv2.VideoCapture(0)
faceClassif: CascadeClassifier = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count: int = 0

while True:
    ret, frame = cap.read()
    if ret == False: break
    frame: any = imutils.resize(frame, width=640)
    gray: None = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aux_Frame: any = frame.copy()
    faces: None = faceClassif.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        rostro: any = aux_Frame[y:y+h, x:x+w]
        rostro: any = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(person_Path + '/rostro_{}_{}.jpg'.format(count, person_Name), rostro)
        count: int = count + 1
    cv2.imshow('frame', frame)

    k: None = cv2.waitKey(1)
    if k == 27 or count >= 100:
        break
