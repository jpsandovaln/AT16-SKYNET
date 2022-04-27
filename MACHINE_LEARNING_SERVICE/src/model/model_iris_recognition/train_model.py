#
# train_model.py Copyright (c) 2022 Jalasoft.
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
from src.model.model_iris_recognition.recognition import Recognition
from src.model.model_iris_recognition.load_image_train import LoadFiles
from src.common.exceptions.execute_exception import ExecuteException
from decouple import config

path_img = config('PATH_IMAGE')
filename = config('FILENAME')
write_bin = 'wb'


# Training the iris recognition
class TrainModel:

    # Training the model
    @staticmethod
    def train_model():
        code_mask_list = []
        images_dic = LoadFiles.load_img_train()
        try:
            for name, imgs in images_dic.items():
                for img in imgs:
                    image2 = img
                    recognition = Recognition()
                    code2, mask2 = recognition.encode_photo(image2)
                    code_mask_list.append([name, code2, mask2])
            outfile = open(filename, write_bin)
            pickle.dump(code_mask_list, outfile)
            outfile.close()
            return 'Model Trained'
        except Exception as error:
            raise ExecuteException(error, "AT16-ERR-302", '400',
                                   'Iris recognition model')