from imageai.Detection import ObjectDetection
from object_result_resnet import ObjectResult
import os


class Resnet:

    def prediction(self, path, word):
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
