#
# @emotion_recognition_controller.py Copyright (c) 2022 Jalasoft.
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

from swagger_server.models.success_emotion_post import SuccessEmotionPost  # noqa: E501
from swagger_server import util


def update_emotion_with_form(file):  # noqa: E501
    """Recognize a face emotion

     # noqa: E501

    :param file: Image file
    :type file: werkzeug.datastructures.FileStorage

    :rtype: SuccessEmotionPost
    """
    return 'do some magic!'
