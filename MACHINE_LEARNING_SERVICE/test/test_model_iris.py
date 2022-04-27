#
# test_model_iris.py Copyright (c)
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

import unittest
from src.model.model_iris_recognition.model_iris import IrisModel
from src.model.model_iris_recognition.train_model import TrainModel


class Testing(unittest.TestCase):

    def test_train_model(self):
        result = TrainModel.train_model()
        self.assertEqual(result, 'Model Trained')

    def test_matching_data(self):
        res = IrisModel("../src/controller/utils/images_iris_recognition/Aquiles/Img_003_L_2.bmp", 1)
        result = res.matching_data()
        self.assertEqual(result, [{'Name': 'Aquiles', 'Percentage': 100.0}])