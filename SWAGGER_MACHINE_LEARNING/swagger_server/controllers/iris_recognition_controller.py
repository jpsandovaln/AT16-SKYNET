#
# @iris_recognition_controller.py Copyright (c) 2022 Jalasoft.
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

from swagger_server.models.success_iris_post import SuccessIrisPost  # noqa: E501
from swagger_server import util


def update_data_with_form(zip):  # noqa: E501
    """Training the model

     # noqa: E501

    :param zip: Upload irises
    :type zip: werkzeug.datastructures.FileStorage

    :rtype: None
    """
    return 'do some magic!'


def update_name_with_form(file, percentage):  # noqa: E501
    """Search a name

     # noqa: E501

    :param file: Upload the iris
    :type file: werkzeug.datastructures.FileStorage
    :param percentage: Percentage between 0-1
    :type percentage: float

    :rtype: SuccessIrisPost
    """
    return 'do some magic!'
