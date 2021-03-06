# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.success_emotion_post import SuccessEmotionPost  # noqa: E501
from swagger_server.test import BaseTestCase


class TestEmotionRecognitionController(BaseTestCase):
    """EmotionRecognitionController integration test stubs"""

    def test_update_emotion_with_form(self):
        """Test case for update_emotion_with_form

        Recognize a face emotion
        """
        data = dict(file=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/emotion',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
