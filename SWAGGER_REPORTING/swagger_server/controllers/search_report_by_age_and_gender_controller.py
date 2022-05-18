#
# @search_report_by_age_and_gender_controller.py Copyright (c) 2022 Jalasoft.
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

from swagger_server.models.success_post import SuccessPost  # noqa: E501
from swagger_server import util


def update_ageand_gender_with_form(person_age, person_gender):  # noqa: E501
    """Search report by age and gender

     # noqa: E501

    :param person_age: Integer eg. 55
    :type person_age: int
    :param person_gender: M or F
    :type person_gender: str

    :rtype: SuccessPost
    """
    return 'do some magic!'
