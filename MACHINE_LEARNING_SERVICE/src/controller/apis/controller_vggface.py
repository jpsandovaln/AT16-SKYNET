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
import ntpath
from src.model.model_vggface import ModelVggFace
from flask import send_file
from PIL import Image
from src.controller.utils.zipfile.decompress import Decompress


class ControllerVggFace:
    def __init__(self, request):
        self.request = request

    # Method that crop and save a face from al image
    def crop_face(self, path):
        photo = self.request.files['file']
        face = ModelVggFace()
        if face.image_has_face(photo):
            face_array = face.extract_face(photo)
            crop_face = Image.fromarray(face_array)
            crop_face.save(os.path.join(path, photo.filename))
            return send_file(os.path.join(path, photo.filename))
        else:
            return 'The image has no recognizable face'

    # Method that compares if 2 persons in 2 images are the same person
    def compare_faces(self):
        face1 = self.request.files['person1']
        face2 = self.request.files['person2']
        file_names = [face1, face2]
        model = ModelVggFace()
        if model.image_has_face(face1) and model.image_has_face(face2):
            embeddings = model.get_embeddings(file_names)
            resp = model.is_match(embeddings[0], embeddings[1])
            value = {
                "Are they the same person?": str(resp)
                }
        else:
            value = self.not_face_in_compare(face1, face2)
        return json.dumps(value)

    def not_face_in_compare(self, image1, image2):
        model = ModelVggFace()
        if not model.image_has_face(image1):
            value = {
                "there is not a face in": str(image1.filename)
            }
        else:
            value = {
                "there is not a face in": str(image2.filename)
            }
        return json.dumps(value)

    # Search a person from an image in a bunch of images from a zip file
    def search_person(self, save_location):
        file_request = self.request.files['file']
        file_person = self.request.files['person']
        path_saved = os.path.join(save_location, file_request.filename)
        file_request.save(path_saved)
        path_zip = Decompress(path_saved)
        path_zip_result = path_zip.path_decompress()
        model = ModelVggFace()
        response = []
        if model.image_has_face(file_person):
            path_files = [(path_zip_result + '''/''' + f) for f in os.listdir(path_zip_result)
                          if os.path.isfile(os.path.join(path_zip_result, f))]
            for file in path_files:
                if model.image_has_face(file):
                    images = [file_person, file]
                    embeddings = model.get_embeddings(images)
                    resp = model.is_match(embeddings[0], embeddings[1])
                    if resp:
                        response.append({
                                "The person appears in": str(ntpath.basename(file))
                            })
        else:
            response = ({
                    "there is not a face in": str(file_person.filename)
                })
        return json.dumps(response)
