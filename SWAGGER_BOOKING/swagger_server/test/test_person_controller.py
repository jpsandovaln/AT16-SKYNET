#
# @test_person_controller.py Copyright (c) 2022 Jalasoft.
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
from swagger_server.models.body_person_post import BodyPersonPost  # noqa: E501
from swagger_server.models.body_person_put import BodyPersonPut  # noqa: E501
from swagger_server.models.success_person_get import SuccessPersonGet  # noqa: E501
from swagger_server.models.success_person_id_get import SuccessPersonIdGet  # noqa: E501
from swagger_server.models.success_person_post import SuccessPersonPost  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPersonController(BaseTestCase):
    """PersonController integration test stubs"""

    def test_get_all(self):
        """Test case for get_all

        Get all Persons of the Database of Booking
        """
        response = self.client.open(
            '/person',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_person_id_id_person_get(self):
        """Test case for person_id_id_person_get

        Get a Person by Id of the Database of Booking
        """
        response = self.client.open(
            '/person/id/{id_person}'.format(id_person='id_person_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_person_id_person_delete(self):
        """Test case for person_id_person_delete

        Delete a Resource by Id of the Database of Booking
        """
        response = self.client.open(
            '/person/{id_person}'.format(id_person='id_person_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_person_id_person_put(self):
        """Test case for person_id_person_put

        Update a Person by Id of the Database of Booking
        """
        body = BodyPersonPut()
        response = self.client.open(
            '/person/{id_person}'.format(id_person='id_person_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_person_name_person_name_get(self):
        """Test case for person_name_person_name_get

        Get a Person by Name of the Database of Booking
        """
        response = self.client.open(
            '/person/name/{person_name}'.format(person_name='person_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_person_post(self):
        """Test case for person_post

        Create a Person into the Database of Booking
        """
        body = BodyPersonPost()
        response = self.client.open(
            '/person',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
