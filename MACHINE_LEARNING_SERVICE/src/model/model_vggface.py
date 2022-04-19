#
# @model_vggface.py Copyright (c) 2022 Jalasoft.
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

# face verification with the VGGFace2 model

from matplotlib import pyplot
from PIL import Image
from numpy import asarray
from scipy.spatial.distance import cosine
from mtcnn.mtcnn import MTCNN
from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input


class ModelVggFace:
    # Extracts the face from an image
    def extract_face(self, filename, required_size=(224, 224)):
        pixels = pyplot.imread(filename)
        detector = MTCNN()
        results = detector.detect_faces(pixels)
        x1, y1, width, height = results[0]['box']
        x2, y2 = x1 + width, y1 + height
        face = pixels[y1:y2, x1:x2]
        image = Image.fromarray(face)
        image = image.resize(required_size)
        face_array = asarray(image)
        return face_array

    # Calculates the embedding for the faces
    def get_embeddings(self, file_names):
        faces = [self.extract_face(f) for f in file_names]
        samples = asarray(faces, 'float32')
        samples = preprocess_input(samples, version=2)
        model = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3),
                        pooling='avg')
        yhat = model.predict(samples)
        return yhat

    # Proves if the face images are from the same person
    def is_match(self, known_embedding, candidate_embedding, thresh=0.5):
        score = cosine(known_embedding, candidate_embedding)
        if score <= thresh:
            print('>face is a Match (%.3f <= %.3f)' % (score, thresh))
            resp = 'Yes'
        else:
            print('>face is NOT a Match (%.3f > %.3f)' % (score, thresh))
            resp = 'No'
        return resp
