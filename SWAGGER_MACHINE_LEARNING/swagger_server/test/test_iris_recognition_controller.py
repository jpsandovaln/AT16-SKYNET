#
# @test_iris_recognition_controller.py Copyright (c) 2022 Jalasoft.
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

from swagger_server.models.success_iris_post import SuccessIrisPost  # noqa: E501
from swagger_server.test import BaseTestCase


class TestIrisRecognitionController(BaseTestCase):
    """IrisRecognitionController integration test stubs"""

    def test_update_data_with_form(self):
        """Test case for update_data_with_form

        Training the model
        """
        data = dict(zip=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/iris_recognition_train',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_name_with_form(self):
        """Test case for update_name_with_form

        Search a name
        """
        data = dict(file=(BytesIO(b'some file data'), 'file.txt'),
                    percentage=3.4)
        response = self.client.open(
            '/iris_recognition',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
