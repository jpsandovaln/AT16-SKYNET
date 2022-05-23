#
# @search_report_fill_time_location_controller.py Copyright (c) 2022 Jalasoft.
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

import connexion
import six

from swagger_server.models.success_location_post import SuccessLocationPost  # noqa: E501
from swagger_server import util


def updatelocation_with_form(start_date, end_date):  # noqa: E501
    """Search the number of reservations for each city within a range of dates

     # noqa: E501

    :param start_date: MM/DD/YYYY eg. 01/18/1995
    :type start_date: str
    :param end_date: MM/DD/YYYY eg. 12/30/2022
    :type end_date: str

    :rtype: SuccessLocationPost
    """
    return 'do some magic!'
