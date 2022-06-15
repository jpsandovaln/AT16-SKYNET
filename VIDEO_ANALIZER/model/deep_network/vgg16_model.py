import os
from model.deep_network.algorithm import Algorithm
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input, decode_predictions
import numpy as np


class VGG16Model(Algorithm):
    def run(self, folder_path, word, min_percentage):
        result = []
        model = VGG16(weights='imagenet', include_top=True)
        for img_name in os.listdir(folder_path):
            full_path = folder_path + img_name
            img1 = image.load_img(folder_path + img_name, target_size=(224, 224))
            x = image.img_to_array(img1)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            prediction = model.predict(x)
            prediction_array = self.find_word(decode_predictions(prediction, top=3)[0], word, img_name, full_path, min_percentage)
            if len(prediction_array) > 0:
                result += prediction_array
        return result

    def find_word(self, result_prediction, word, file_name, image_path, min_percentage):
        result = []
        print(result_prediction)
        for prediction in result_prediction:
            percentage = round(prediction[2] * 100, 2)
            if len(prediction) > 0 and word in prediction[1] and percentage >= float(min_percentage):
                result.append(
                    {
                        'word': prediction[1],
                        'percentage': '{}%'.format(percentage),
                        'second': os.path.splitext(file_name)[0],
                        'image': image_path
                    }
                )
        return result
