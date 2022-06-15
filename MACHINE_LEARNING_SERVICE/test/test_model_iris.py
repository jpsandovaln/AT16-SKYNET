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
import pathlib
import unittest
from unittest.mock import patch
from src.model.model_iris_recognition.model_iris import IrisModel
from src.model.model_iris_recognition.train_model import TrainModel
from src.controller.apis.controller_iris_recognizer import ControllerIris
from src.model.model_iris_recognition.parameters import Parameters
from src.common.exceptions.parameter_exception import ParameterException
from src.common.exceptions.machine_learning_exception import MachineLearningException


class Testing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.folder_file = pathlib.Path(__file__).parent.absolute()
        cls.path_file = pathlib.Path.joinpath(cls.folder_file, 'resources/Img_037_L_4.bmp')

    def test_train_model(self):
        result = TrainModel.train_model()
        self.assertEqual(result, 'Model Trained')

    # The model must be trained whit Donald iris for the following test
    def test_matching_data(self):
        res = IrisModel(str(self.path_file), '1')
        result = res.matching_data()
        self.assertEqual(result, [{'Name': 'Donald', 'Percentage': 100.0}])

    def test_iris_validate_file(self):
        with self.assertRaises(MachineLearningException):
            test_file = IrisModel('', 1)
            test_file.matching_data()

    # valid a non number as a percentage
    def test_iris_validate_percentage_non_number(self):
        with self.assertRaises(MachineLearningException):
            test_file = IrisModel(str(self.path_file), "NonNumber")
            test_file.matching_data()

    # valid a number higher than 1 as a percentage
    def test_iris_validate_percentage_higher(self):
        with self.assertRaises(MachineLearningException):
            test_file = IrisModel(str(self.path_file), '8')
            test_file.matching_data()
