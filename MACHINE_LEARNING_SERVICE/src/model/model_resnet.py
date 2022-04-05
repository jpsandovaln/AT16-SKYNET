#
# @model_resnet.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
from imageai.Detection import ObjectDetection
from Result.object_result import ObjectResult
import os


class Resnet:
# Class that represent to the Object Recognition Model

    def prediction(self, path, word):

        # Method that return a list with the objects predicted
        output_path = "./output/newimage.jpg"
        list_object_result = []
        execution_path = os.getcwd()
        detector = ObjectDetection()
        detector.setModelTypeAsRetinaNet()
        detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.1.0.h5"))
        detector.loadModel()
        path_files = [(path + "\\" + f) for f in os.listdir(path)
                      if os.path.isfile(os.path.join(path, f))]
        for file in path_files:
            detections = detector.detectObjectsFromImage(input_image=file, output_image_path=output_path)

            # Fill the list with results that match to the Word variable
            for eachObject in detections:
                if eachObject["name"] == word and eachObject["percentage_probability"] >= 70:
                    name_obj = eachObject["name"]
                    percentage = eachObject["percentage_probability"]
                    object_result = ObjectResult()
                    object_result.set_name(name_obj)
                    object_result.set_percentage(percentage)
                    object_result.set_path_file(file)
                    list_object_result.append(object_result)
        i = 0
        return list_object_result
