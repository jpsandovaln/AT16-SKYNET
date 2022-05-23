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
from typing import TextIO

from src.model.model_iris_recognition.parameters import Parameters
from src.model.model_iris_recognition.recognition import Recognition
from src.model.model_iris_recognition.load_image_person import LoadFiles
from decouple import config


filename = config('FILENAME')
read_bin = 'rb'


# Iris recognition model
class IrisModel:
    def __init__(self, file: any, percentage: float):
        self.file: any = file
        self.percentage: float = percentage

    # Matching the data in order to return the name to which the iris belongs.
    def matching_data(self) -> list[dict[str, float]]:
        parameters: Parameters = Parameters(self.file, self.percentage)
        parameters.validate()
        person_result: list[dict[str, float]] = []
        load_files: LoadFiles = LoadFiles(self.file)
        image: None = load_files.load_img_compare()
        recognition: Recognition = Recognition()
        code, mask = recognition.encode_photo(image)
        infile: TextIO = open(filename, read_bin)
        code_mask_list: any = pickle.load(infile)
        infile.close()
        for codes in code_mask_list:
            name: any = codes[0]
            code2: any = codes[1]
            mask2: any = codes[2]
            jaccard_index: float = 1 - recognition.compare_codes(code, code2, mask, mask2)
            if jaccard_index >= float(self.percentage):
                person_result.append({"Name": name, "Percentage": round(
                    jaccard_index * 100, 1)})
        return person_result

