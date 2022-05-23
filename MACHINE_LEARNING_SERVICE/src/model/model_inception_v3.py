#
# @model_inception_v3.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Condidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#


import os
from datetime import datetime
from operator import __add__
from tkinter import Image

import keras
from keras import Model
from keras.applications.inception_v3 import InceptionV3, decode_predictions
from keras.preprocessing.image import load_img, img_to_array
from src.model.Result.object_result import ObjectResult


class ModelInceptionV3:
    """Class that represent to the Object Recognition Model"""

    def prediction(self, path: {__add__}, word: any, percentage: object) -> dict[str, dict[str, str | float]]:
        """Method that return a list with the objects predicted"""

        # List of the objects predicted
        list_object_result: list[ObjectResult] = []

        # Load the model
        model: Model = InceptionV3()

        # Create the paths for the images
        path_files: list = [(path + "\\" + f) for f in os.listdir(path)
                            if os.path.isfile(os.path.join(path, f))]

        # Predict the objects that are in the images
        for file in path_files:
            image: Image = load_img(file, target_size=(299, 299))
            image: Image = img_to_array(image)
            image: Image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
            image: Image = keras.applications.inception_v3.preprocess_input(image)
            result_prediction: any = model.predict(image)
            result: list[list[tuple[any, ...]]] = decode_predictions(result_prediction, top=10)

            # Fill the list with results that match to the Word variable
            for predictions in result:
                for object_predicted in predictions:
                    if object_predicted[1] == word and object_predicted[2] >= float(percentage):
                        object_result: ObjectResult = ObjectResult()
                        object_result.set_id_object(object_predicted[0])
                        object_result.set_name(object_predicted[1])
                        object_result.set_percentage(object_predicted[2])
                        object_result.set_path_file(file)
                        list_object_result.append(object_result)

        object_dict: dict[str, dict[str, str | float]] = {}
        num_obj: int = 1
        for object_result in list_object_result:
            path: any = object_result.get_path_file()
            normalized_path: str = os.path.normpath(path)
            path_components = normalized_path.split(os.sep)
            img = path_components[-1]
            try:
                time_img: int = int(img[:-4])
                convert_time: str = str(datetime.timedelta(seconds=time_img))
            except:
                convert_time: str = img[:-4]

            object_dict["Object " + str(num_obj)]: dict[str, dict[str, str | float]] = {
                "Name": object_result.get_name(),
                "Time": convert_time,
                "Percentage": object_result.get_percentage() * 100}
            num_obj += 1
        return object_dict
