#
# @test_extract_data_from_mongo_and_load_into_psql_controller.py
# Copyright (c) 2022 Jalasoft.
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

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestExtractDataFromMongoAndLoadIntoPsqlController(BaseTestCase):
    """ExtractDataFromMongoAndLoadIntoPsqlController integration test stubs"""

    def test_get_data_base_with_form(self):
        """Test case for get_data_base_with_form

        Extract data from Mongo and load into Psql
        """
        response = self.client.open(
            '/mongo_to_postgres',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
