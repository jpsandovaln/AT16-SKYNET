#
# @test_search_report_by_state_and_gender_controller.py Copyright (c)
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

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.success_post import SuccessPost  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSearchReportByStateAndGenderController(BaseTestCase):
    """SearchReportByStateAndGenderController integration test stubs"""

    def test_update_state_with_form(self):
        """Test case for update_state_with_form

        Search report by state and gender
        """
        data = dict(state='state_example',
                    person_gender='person_gender_example')
        response = self.client.open(
            '/search_report_state_person_gender',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
