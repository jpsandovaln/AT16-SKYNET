#
# @controller_vggface.py Copyright (c) 2022 Jalasoft.
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

import json
import os
from src.model.model_vggface import ModelVggFace
from flask import send_file
from PIL import Image


class ControllerVggFace:
    def __init__(self, request):
        self.request = request

    # Method that crop and save a face from al image
    def crop_face(self):
        photo = self.request.files['file']
        face = ModelVggFace()
        face_array = face.extract_face(photo)
        crop_face = Image.fromarray(face_array)
        crop_face.save(os.path.join('saved_files/vggface_files', photo.filename))
        return send_file(os.path.join('saved_files/vggface_files', photo.filename))

    # Method that compares if 2 persons in 2 images are the same person
    def compare_faces(self):
        face1 = self.request.files['person1']
        face2 = self.request.files['person2']
        filenames = [face1, face2]
        model = ModelVggFace()
        embeddings = model.get_embeddings(filenames)
        resp = model.is_match(embeddings[0], embeddings[1])
        value = {
            "Are they the same person?": resp
            }
        return json.dumps(value)
