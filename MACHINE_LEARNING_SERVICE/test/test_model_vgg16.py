#
# @test_model_vgg16.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import unittest
from src.model.model_vgg16 import ModelVgg16


# Method to search the name of the object in the list of result
def search_object(list_object_result, object_searched):
    is_found = False
    for object_result in list_object_result:
        if object_result.get_name() == object_searched:
            is_found = True
            break
    return is_found


class ModelTest(unittest.TestCase):

    # Test to search a pickup
    def test_search_a_pickup(self):
        object_searched = "pickup"
        model_vgg16 = ModelVgg16()
        list_object_result = model_vgg16.predict(r"..\src\controller\utils\images_vgg16",
                                                 object_searched, 0.2)
        is_found = search_object(list_object_result, object_searched)
        self.assertTrue(True, is_found)

    # Test to search a husky
    def test_search_a_husky(self):
        object_searched = "Siberian_husky"
        model_vgg16 = ModelVgg16()
        list_object_result = model_vgg16.predict(r"..\src\controller\utils\images_vgg16",
                                                 object_searched, 0.2)
        is_found = search_object(list_object_result, object_searched)
        self.assertTrue(True, is_found)

    # Test to search a image of refrigerator
    def test_search_refrigerator(self):
        object_searched = "refrigerator"
        model_vgg16 = ModelVgg16()
        list_object_result = model_vgg16.predict(r"..\src\utils\images_vgg16", object_searched)
        is_found = search_object(list_object_result, object_searched)
        self.assertTrue(True, is_found)
