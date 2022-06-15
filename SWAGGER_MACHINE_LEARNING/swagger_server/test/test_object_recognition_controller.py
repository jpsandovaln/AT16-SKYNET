# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.success_object_recognition_post import SuccessObjectRecognitionPost  # noqa: E501
from swagger_server.test import BaseTestCase


class TestObjectRecognitionController(BaseTestCase):
    """ObjectRecognitionController integration test stubs"""

    def test_update_object_with_form(self):
        """Test case for update_object_with_form

        Search an object
        """
        data = dict(file=(BytesIO(b'some file data'), 'file.txt'),
                    name='name_example',
                    model='model_example',
                    percentage=3.4)
        response = self.client.open(
            '/object_recognizer',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
