#
# @model_iris.py Copyright (c) 2022 Jalasoft.
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

import pickle
from src.model.model_iris_recognition.parameters import Parameters
from src.model.model_iris_recognition.recognition import Recognition
from src.model.model_iris_recognition.load_image_person import LoadFiles
from decouple import config


filename = config('FILENAME')
read_bin = 'rb'


# Iris recognition model
class IrisModel:
    def __init__(self, file, percentage):
        self.file = file
        self.percentage = percentage

    # Matching the data in order to return the name to which the iris belongs.
    def matching_data(self):
        parameters = Parameters(self.file, self.percentage)
        parameters.validate()
        person_result = []
        load_files = LoadFiles(self.file)
        image = load_files.load_img_compare()
        recognition = Recognition()
        code, mask = recognition.encode_photo(image)
        infile = open(filename, read_bin)
        code_mask_list = pickle.load(infile)
        infile.close()
        for codes in code_mask_list:
            name = codes[0]
            code2 = codes[1]
            mask2 = codes[2]
            jaccard_index = 1 - recognition.compare_codes(code, code2, mask, mask2)
            if jaccard_index >= float(self.percentage):
                person_result.append({"Name": name, "Percentage": round(
                    jaccard_index * 100, 1)})
        return person_result

