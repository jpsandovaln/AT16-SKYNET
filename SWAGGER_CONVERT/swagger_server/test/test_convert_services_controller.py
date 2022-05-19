#
# @test_convert_services_controller.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Condidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.success_convert_post import SuccessConvertPost  # noqa: E501
from swagger_server.test import BaseTestCase


class TestConvertServicesController(BaseTestCase):
    """ConvertServicesController integration test stubs"""

    def test_add_file(self):
        """Test case for add_file

        Add a new file deppending of service
        """
        data = dict(convert='Audio',
                    file=(BytesIO(b'some file data'), 'file.txt'),
                    bitrate=4000,
                    sample_rate=24000,
                    audio_chanel=2,
                    frame=1,
                    color='RGB',
                    height=1000,
                    width=1000,
                    rotate=1,
                    vertical_flip=1,
                    horizontal_flip=0,
                    language_in='en-EN',
                    language_out='es-ES',
                    language='eng',
                    format='wav')
        response = self.client.open(
            '/convert',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
