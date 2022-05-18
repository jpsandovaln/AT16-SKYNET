# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.success_post import SuccessPost  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSearchReportByAgeAndGenderController(BaseTestCase):
    """SearchReportByAgeAndGenderController integration test stubs"""

    def test_update_ageand_gender_with_form(self):
        """Test case for update_ageand_gender_with_form

        Search report by age and gender
        """
        data = dict(person_age=789,
                    person_gender='person_gender_example')
        response = self.client.open(
            '/search_report_age_gender',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
