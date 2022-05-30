#
# @test_face_recognition_controller.py Copyright (c) 2022 Jalasoft.
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
