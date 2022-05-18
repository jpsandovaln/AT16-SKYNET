#
# @search_report_by_type_and_model_controller.py Copyright (c) 2022 Jalasoft.
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


def update_report_type_with_form(type, model):  # noqa: E501
    """Search report by type and model

     # noqa: E501

    :param type: String eg. Asus
    :type type: str
    :param model: String eg. Jeep
    :type model: str

    :rtype: SuccessPost
    """
    return 'do some magic!'
