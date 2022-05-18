# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.success_country_post import SuccessCountryPost  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSearchReservationsForEachCountryByRangeOfDateController(BaseTestCase):
    """SearchReservationsForEachCountryByRangeOfDateController integration test stubs"""

    def test_update_country_with_form(self):
        """Test case for update_country_with_form

        Search the number of reservations for each country within a range of dates
        """
        data = dict(start_date='start_date_example',
                    end_date='end_date_example')
        response = self.client.open(
            '/search_report_date_person_country',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
