# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.success_post import SuccessPost  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSearchReportByTypeAndModelController(BaseTestCase):
    """SearchReportByTypeAndModelController integration test stubs"""

    def test_update_report_type_with_form(self):
        """Test case for update_report_type_with_form

        Search report by type and model
        """
        data = dict(type='type_example',
                    model='model_example')
        response = self.client.open(
            '/search_report_model_type',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
