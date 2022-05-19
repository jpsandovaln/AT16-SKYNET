#
# @test_resource_controller.py Copyright (c) 2022 Jalasoft.
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
from swagger_server.models.body_resource_post import BodyResourcePost  # noqa: E501
from swagger_server.models.body_resource_put import BodyResourcePut  # noqa: E501
from swagger_server.models.success_resource_get import SuccessResourceGet  # noqa: E501
from swagger_server.models.success_resource_id_get import SuccessResourceIdGet  # noqa: E501
from swagger_server.models.success_resource_post import SuccessResourcePost  # noqa: E501
from swagger_server.test import BaseTestCase


class TestResourceController(BaseTestCase):
    """ResourceController integration test stubs"""

    def test_deleteresource(self):
        """Test case for deleteresource

        Delete a Resource by Id of the Database of Booking
        """
        response = self.client.open(
            '/resource/{id_resource}'.format(id_resource='id_resource_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_findresource(self):
        """Test case for findresource

        Find a resource
        """
        response = self.client.open(
            '/resource',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_findresourcebyid(self):
        """Test case for findresourcebyid

        Find a resource by id
        """
        response = self.client.open(
            '/resource/id/{id_resource}'.format(id_resource='id_resource_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_findresourcebyname(self):
        """Test case for findresourcebyname

        Find a resource by name
        """
        response = self.client.open(
            '/resource/name/{resource_name}'.format(resource_name='resource_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_insertresource(self):
        """Test case for insertresource

        Insert a resource
        """
        body = BodyResourcePost()
        response = self.client.open(
            '/resource',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_updateresource(self):
        """Test case for updateresource

        Update a Resource by Id
        """
        body = BodyResourcePut()
        response = self.client.open(
            '/resource/{id_resource}'.format(id_resource='id_resource_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
