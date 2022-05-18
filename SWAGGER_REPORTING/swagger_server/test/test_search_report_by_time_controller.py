#
# @test_search_report_by_time_controller.py Copyright (c) 2022 Jalasoft.
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

from swagger_server.models.success_gender_post import SuccessGenderPost  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSearchReportByTimeController(BaseTestCase):
    """SearchReportByTimeController integration test stubs"""

    def test_update_gender_with_form(self):
        """Test case for update_gender_with_form

        Search the number of reservations made in the morning and afternoon for each gender
        """
        data = dict(open_time='open_time_example',
                    close_time='close_time_example')
        response = self.client.open(
            '/search_report_start_finish_time_person_gender',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
