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
import keras
from keras.applications.inception_v3 import InceptionV3, decode_predictions
from keras.preprocessing.image import load_img, img_to_array
from MACHINE_LEARNING_SERVICE.src.classes.object_result import ObjectResult


class ModelInceptionV3:
    """Class that represent to the Object Recognition Model"""

    def prediction(self, path, word):
        """Method that return a list with the objects predicted"""

        # List of the objects predicted
        list_object_result = []

        # Load the model
        model = InceptionV3()

        # Create the paths for the images
        path_files = [(path + "\\" + f) for f in os.listdir(path)
                      if os.path.isfile(os.path.join(path, f))]

        # Predict the objects that are in the images
        for file in path_files:
            image = load_img(file, target_size=(299, 299))
            image = img_to_array(image)
            image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
            image = keras.applications.inception_v3.preprocess_input(image)
            result_prediction = model.predict(image)
            result = decode_predictions(result_prediction, top=10)

            # Fill the list with results that match to the Word variable
            for predictions in result:
                for object_predicted in predictions:
                    if object_predicted[1] == word and object_predicted[2] >= 0.2:
                        object_result = ObjectResult()
                        object_result.set_id_object(object_predicted[0])
                        object_result.set_name(object_predicted[1])
                        object_result.set_percentage(object_predicted[2])
                        object_result.set_path_file(file)
                        list_object_result.append(object_result)

        object_array = []
        for object_result in list_object_result:
            object_array.append((object_result.get_path_file(),
                                 object_result.get_name(),
                                 str(round(
                                     object_result.get_percentage() * 100))))
        return object_array



