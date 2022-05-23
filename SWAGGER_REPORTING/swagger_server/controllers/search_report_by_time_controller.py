#
# @search_report_by_time_controller.py Copyright (c) 2022 Jalasoft.
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

from swagger_server.models.success_gender_post import SuccessGenderPost  # noqa: E501
from swagger_server import util


def update_gender_with_form(open_time, close_time):  # noqa: E501
    """Search the number of reservations made in the morning and afternoon for each gender

     # noqa: E501

    :param open_time: HH:MM:SS eg. 08:30:00
    :type open_time: str
    :param close_time: HH:MM:SS eg. 18:30:00
    :type close_time: str

    :rtype: SuccessGenderPost
    """
    return 'do some magic!'
