#
# @controller_machine.py Copyright (c) 2022 Jalasoft.
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

from src.model.model_vgg16 import ModelVgg16
from src.model.model_inception_v3 import ModelInceptionV3
#from src.model.model_resnet import Resnet
import json


# Returns a list of images that contain the word.
class ModelResult:
    def __init__(self, save_location, name_request, model_request, percentage_request):
        self.name_request = name_request
        self.save_location = save_location
        self.model_request = model_request
        self.percentage_request = percentage_request

    # Returns a list of images that contain the word.
    def models_results(self):
        if self.model_request == 'ModelVgg16':
            model_vgg16 = ModelVgg16()
            list_object_result = model_vgg16.predict(self.save_location, self.name_request,
                                                     self.percentage_request)
            dic_json = json.dumps(list_object_result, indent=4)
            return dic_json

        elif self.model_request == 'InceptionV3':
            inception_v3_match = ModelInceptionV3()
            list_object_result = inception_v3_match.prediction(self.save_location, self.name_request,
                                                               self.percentage_request)
            dic_json = json.dumps(list_object_result, indent=4)
            return dic_json

        # elif self.model_request == 'Resnet':
        #     model_resnet = Resnet()
        #     list_object_result = model_resnet.prediction(self.save_location, self.name_request,
        #                                                  self.percentage_request)
        #     dic_json = json.dumps(list_object_result, indent=4)
        #     return dic_json
