#
# test_inceptionV3.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
#1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
#All rights reserved.
#
#This software is the confidential and proprietary information of
#Jalasoft, ("Condidential Information"). You shall # not
#disclose such Confidential Information and shall use it only in
#accordance with the terms of the license agreement you entered into
#with Jalasoft.
#


import unittest
from src.model_inception_v3 import ModelInceptionV3

class InceptionV3Test(unittest.TestCase):

    def test_match_image_beach_wagon(self):
        inception_v3_match = ModelInceptionV3()
        result = inception_v3_match.prediction(r"C:/Users/Abraham/Documents/inceptonV3/src/utils/images_inceptionV3",
                                               "pug")
        self.assertEqual(result.get_name(), "pug")
