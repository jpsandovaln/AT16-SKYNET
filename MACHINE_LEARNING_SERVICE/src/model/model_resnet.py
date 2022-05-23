#
# @model_vgg16.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import datetime
from imageai.Detection import ObjectDetection
from src.model.Result.object_result import ObjectResult
import os


class Resnet:
    """Class that represent to the Object Recognition Model"""

    def prediction(self, path: any, word: any, per: any) -> dict[str, dict[str, str | float]]:

        """Method that return a list with the objects predicted"""

        output_path: str = "./output/newimage.jpg"
        list_object_result: list[ObjectResult] = []
        execution_path: str = os.getcwd()
        detector: ObjectDetection = ObjectDetection()
        detector.setModelTypeAsRetinaNet()
        detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.1.0.h5"))
        detector.loadModel()
        path_files: list = [(path + "\\" + f) for f in os.listdir(path)
                            if os.path.isfile(os.path.join(path, f))]
        for file in path_files:
            detections: tuple = detector.detectObjectsFromImage(input_image=file, output_image_path=output_path)
            for eachObject in detections:
                if eachObject["name"] == word and eachObject["percentage_probability"] >= float(per):
                    name_obj: any = eachObject["name"]
                    percentage: float = eachObject["percentage_probability"]
                    object_result: ObjectResult = ObjectResult()
                    object_result.set_name(name_obj)
                    object_result.set_percentage(percentage)
                    object_result.set_path_file(file)
                    list_object_result.append(object_result)

        object_dict: dict[str, dict[str, str | float]] = {}
        num_obj: int = 1
        for object_result in list_object_result:
            path: any = object_result.get_path_file()
            normalized_path: str = os.path.normpath(path)
            path_components: list[str] = normalized_path.split(os.sep)
            img: str = path_components[-1]
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
