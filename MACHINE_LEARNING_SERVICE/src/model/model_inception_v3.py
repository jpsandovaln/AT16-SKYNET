#
# @model_inception_v3.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
#1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
#All rights reserved.
#
#This software is the confidential and proprietary information of
#Jalasoft, ("Condidential Information"). You shall # not
#disclose such Confidential Information and shall use it only in
#accordance with the terms of the license agreement you entered into
#with Jalasoft.
#


import os
import keras
from keras.applications.inception_v3 import InceptionV3, decode_predictions
from keras.preprocessing.image import load_img, img_to_array
from Result.object_result import ObjectResult

class ModelInceptionV3:
    def select_img_in_folder(self, path: str):
        content = os.listdir(path)
        imgs = []
        for file in content:
            if os.path.isfile(os.path.join(path, file)) and file.endswith('.jpg'):
                imgs.append(file)
        complete_path = str(path) + "/" + str(imgs[0])
        return complete_path

    def prediction(self, complete_path, word):
        this_word = word
        path = complete_path

        filename = ModelInceptionV3.select_img_in_folder(self, path)

        iv3 = InceptionV3()
        target_size = (299, 299)
        img = load_img(filename, target_size=target_size)
        x = img_to_array(img)
        x = x.reshape([1, x.shape[0], x.shape[1], x.shape[2]])
        keras.applications.inception_v3.preprocess_input(x)
        y = iv3.predict(x)
        raw_data = decode_predictions(y)

        object_result = ObjectResult()
        object_result.set_name(raw_data[0][0][1])
        object_result.set_percentage("{:.0%}".format(raw_data[0][0][2]))
        object_result.set_path_file(filename)
        return object_result




