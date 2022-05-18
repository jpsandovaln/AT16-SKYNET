# coding: utf-8

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
