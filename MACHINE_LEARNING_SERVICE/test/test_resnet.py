#
# test_inceptionV3.py Copyright (c)
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
from MACHINE_LEARNING_SERVICE.src.model_resnet import Resnet


class Testing(unittest.TestCase):

    def test_prediction_name(self):
        resnet = Resnet()
        result = resnet.prediction("./input/image.jpg", "dog")
        self.assertEqual(result.get_name(), "dog")

    def test_prediction_percentaje(self):
        resnet = Resnet()
        result = resnet.prediction("./input/image.jpg", "dog")
        self.assertEqual(result.get_percentage(), "92.02658534049988")

