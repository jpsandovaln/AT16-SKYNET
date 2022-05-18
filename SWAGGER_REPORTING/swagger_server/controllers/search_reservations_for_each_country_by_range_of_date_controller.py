#
# @search_reservations_for_each_country_by_range_of_date_controller.py
# Copyright (c) 2022 Jalasoft.
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

from swagger_server.models.success_country_post import SuccessCountryPost  # noqa: E501
from swagger_server import util


def update_country_with_form(start_date, end_date):  # noqa: E501
    """Search the number of reservations for each country within a range of dates

     # noqa: E501

    :param start_date: MM/DD/YYYY eg. 01/18/1995
    :type start_date: str
    :param end_date: MM/DD/YYYY eg. 01/18/2019
    :type end_date: str

    :rtype: SuccessCountryPost
    """
    return 'do some magic!'
