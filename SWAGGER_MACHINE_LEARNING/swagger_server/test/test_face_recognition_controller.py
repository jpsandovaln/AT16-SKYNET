# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.success_face_recognition_post import SuccessFaceRecognitionPost  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFaceRecognitionController(BaseTestCase):
    """FaceRecognitionController integration test stubs"""

    def test_update_face_with_form(self):
        """Test case for update_face_with_form

        Search an object
        """
        data = dict(file=(BytesIO(b'some file data'), 'file.txt'),
                    person=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/vggface_search_person',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
