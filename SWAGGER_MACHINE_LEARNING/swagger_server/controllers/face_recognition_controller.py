#
# @face_recognition_controller.py Copyright (c) 2022 Jalasoft.
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

from swagger_server.models.success_face_recognition_post import SuccessFaceRecognitionPost  # noqa: E501
from swagger_server import util


def update_face_with_form(file, person):  # noqa: E501
    """Search an object

     # noqa: E501

    :param file: Zip file
    :type file: werkzeug.datastructures.FileStorage
    :param person: Image of person face to search
    :type person: werkzeug.datastructures.FileStorage

    :rtype: SuccessFaceRecognitionPost
    """
    return 'do some magic!'
