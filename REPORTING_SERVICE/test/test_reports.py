#
# @test_reports.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from unittest import TestCase, mock
import pandas as pd
import json
from src.controller.apis.search_report_age_gender import SearchReportAgeGender
from src.controller.apis.search_report_model_type import SearchReportModelType
from src.controller.apis.search_report_state_person_gender import SearchReportStatePersonGender
from src.reporting.criteria.criteria import Criteria
from src.reporting.parameters.parameter_report_age_gender import ParameterReportAgeGender
from src.reporting.parameters.parameter_report_model_type import ParameterReportModelType
from src.reporting.parameters.parameter_report_state_person_gender import \
    ParameterReportStatePersonGender


def load_json_expected_result(path):

    # Load de expected results in expected_result variable
    with open(path) as answer_age_gender:
        expected_result = json.load(answer_age_gender)
    return json.dumps(expected_result)


class TestReports(TestCase):

    def setUp(self):
        # Load the data
        file_name = '../test/resources/test_reporting.csv'
        self.data = pd.read_csv(file_name, header=0, sep=';')

    # Test to verify that the report_age_gender
    @mock.patch('src.reporting.criteria.criteria.Criteria.get_df')
    def test_report_age_gender(self, mock_get_df):

        # Defines parameters, minor to 40 and gender equal to M
        age = '40'
        gender = 'M'
        mock_get_df.return_value = self.data
        parameters = ParameterReportAgeGender(age, gender, Criteria.get_df())
        message_error = "The result report is not equal to expected result"

        # Loads de expected results in expected_result variable
        expected_result = load_json_expected_result('resources/expected_age_40_gender_M.json')

        # Gets the report result in actual_result variable
        actual_result = SearchReportAgeGender().search_report_age_gender(parameters)


        self.assertTrue(actual_result == expected_result, message_error)

    @mock.patch('src.reporting.criteria.criteria.Criteria.get_df')
    def test_report_age_gender_2(self, mock_get_df):

        # Define parameters, minor to 40 and gender equal to M
        age = '20'
        gender = 'F'
        mock_get_df.return_value = self.data
        parameters = ParameterReportAgeGender(age, gender, Criteria.get_df())
        message_error = "The result report is not equal to expected result"

        # Load de expected results in expected_result variable
        expected_result = load_json_expected_result('resources/expected_age_20_gender_F.json')

        # Get the report result in actual_result variable
        actual_result = SearchReportAgeGender().search_report_age_gender(parameters)

        self.assertTrue(actual_result == expected_result, message_error)

    @mock.patch('src.reporting.criteria.criteria.Criteria.get_df')
    def test_search_report_state_person_gender(self, mock_get_df):

        # Define parameters, state equal to booked and gender equal to M
        state = 'booked'
        gender = 'F'
        mock_get_df.return_value = self.data
        parameters = ParameterReportStatePersonGender(gender, state, Criteria.get_df())
        message_error = "The result report is not equal to expected result"

        # Load de expected results in expected_result variable
        expected_result = load_json_expected_result('resources/expected_state_Booked_gender_F.json')

        # Get the report result in actual_result variable
        actual_result = SearchReportStatePersonGender().\
            search_report_state_person_gender(parameters)

        self.assertTrue(actual_result == expected_result, message_error)

    @mock.patch('src.reporting.criteria.criteria.Criteria.get_df')
    def test_search_report_model_type(self, mock_get_df):
        # Defines parameters, state equal to booked and gender equal to M
        resource_type = 'vehicles'
        resource_model = 'Jeep'
        path_result = 'resources/expected_model_jeep_type_vehicles.json'
        mock_get_df.return_value = self.data
        parameters = ParameterReportModelType(resource_model, resource_type, Criteria.get_df())

        message_error = "The result report is not equal to expected result"

        # Loads the expected results in expected_result variable
        expected_result = load_json_expected_result(path_result)

        # Gets the report result in actual_result variable
        actual_result = SearchReportModelType().search_report_model_type(parameters)
        self.assertTrue(actual_result == expected_result, message_error)
