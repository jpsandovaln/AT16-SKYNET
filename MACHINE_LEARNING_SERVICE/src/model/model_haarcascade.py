import cv2
import os

class ModelHaarcascade:

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def face_recognizer(self):
        path2 = r''+self.path
        data_Path = r'C:\Skynet\AT16-SKYNET\MACHINE_LEARNING_SERVICE\src\controller\utils\images_haarcascade'
        image_Paths = os.listdir(data_Path)
        print('image_Paths = ', image_Paths)

        face_Recognizer = cv2.face.EigenFaceRecognizer_create()
        face_Recognizer.read(r'C:\Skynet\AT16-SKYNET\MACHINE_LEARNING_SERVICE\src\model\ModelTraining.xml')
        # cap = cv2.VideoCapture(0)
        cap = cv2.VideoCapture(path2)
        face_Classif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        while True:
            ret, frame = cap.read()
            if ret == False: break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            aux_Frame = gray.copy()
            faces = face_Classif.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                rostro = aux_Frame[y:y + h, x:x + w]
                rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
                result = face_Recognizer.predict(rostro)

                # cv2.putText(frame, '{}'.format(result), (x, y-5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)
                if image_Paths[result[0]] == self.name:
                    cv2.putText(frame, '{}'.format(image_Paths[result[0]]), (x, y - 25), 2, 1.1, (0, 255, 0), 1,
                                cv2.LINE_AA)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                else:
                    cv2.putText(frame, 'Desconocido', (x, y - 20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            cv2.imshow('frame', frame)
            Key = cv2.waitKey(1)
            if Key == 27:
                break

        cap.release()
        cv2.destroyAllWindows()
        return 'si sirve'
