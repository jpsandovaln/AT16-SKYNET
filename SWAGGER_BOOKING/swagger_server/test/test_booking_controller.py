#
# @test_booking_controller.py Copyright (c) 2022 Jalasoft.
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
from swagger_server.models.body_booking_post import BodyBookingPost  # noqa: E501
from swagger_server.models.body_booking_put import BodyBookingPut  # noqa: E501
from swagger_server.models.success_booking_get import SuccessBookingGet  # noqa: E501
from swagger_server.models.success_booking_post import SuccessBookingPost  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBookingController(BaseTestCase):
    """BookingController integration test stubs"""

    def test_booking_get(self):
        """Test case for booking_get

        Get all booking of the DataBase
        """
        response = self.client.open(
            '/booking',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_booking_id_booking_delete(self):
        """Test case for booking_id_booking_delete

        Delete a booking of the DataBase
        """
        response = self.client.open(
            '/booking/{id_booking}'.format(id_booking='id_booking_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_booking_id_booking_put(self):
        """Test case for booking_id_booking_put

        Update a Booking by Id
        """
        body = BodyBookingPut()
        response = self.client.open(
            '/booking/{id_booking}'.format(id_booking='id_booking_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_booking_id_id_booking_get(self):
        """Test case for booking_id_id_booking_get

        Get a Booking by Id
        """
        response = self.client.open(
            '/booking/id/{id_booking}'.format(id_booking='id_booking_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_booking_post(self):
        """Test case for booking_post

        Create a Booking
        """
        body = BodyBookingPost()
        response = self.client.open(
            '/booking',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
