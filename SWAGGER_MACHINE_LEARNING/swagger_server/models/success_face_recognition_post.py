#
# @success_face_recognition_post.py Copyright (c) 2022 Jalasoft.
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

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object2 import Object2
from swagger_server import util


class SuccessFaceRecognitionPost(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, array: Object2=None):  # noqa: E501
        """SuccessFaceRecognitionPost - a model defined in Swagger

        :param array: The array of this SuccessFaceRecognitionPost.  # noqa: E501
        :type array: Object2
        """
        self.swagger_types = {
            'array': Object2
        }

        self.attribute_map = {
            'array': 'array'
        }

        self._array = array

    @classmethod
    def from_dict(cls, dikt) -> 'SuccessFaceRecognitionPost':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SuccessFaceRecognitionPost of this SuccessFaceRecognitionPost.  # noqa: E501
        :rtype: SuccessFaceRecognitionPost
        """
        return util.deserialize_model(dikt, cls)

    @property
    def array(self) -> Object2:
        """Gets the array of this SuccessFaceRecognitionPost.


        :return: The array of this SuccessFaceRecognitionPost.
        :rtype: Object2
        """
        return self._array

    @array.setter
    def array(self, array: Object2):
        """Sets the array of this SuccessFaceRecognitionPost.


        :param array: The array of this SuccessFaceRecognitionPost.
        :type array: Object2
        """

        self._array = array