from imageai.Detection import ObjectDetection
from object_result_resnet import ObjectResult
import os


class Resnet:

    def prediction(self, input_path, word):
        output_path = "./output/newimage.jpg"
        execution_path = os.getcwd()
        detector = ObjectDetection()
        detector.setModelTypeAsRetinaNet()
        detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.1.0.h5"))
        detector.loadModel()
        detections = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)

        for eachObject in detections:
            if eachObject["name"] == word:
                name_obj=eachObject["name"]
                percentage=eachObject["percentage_probability"]
                object_result = ObjectResult()
                object_result.set_name(name_obj)
                object_result.set_percentage(percentage)
                object_result.set_path_file(input_path)
                return object_result
