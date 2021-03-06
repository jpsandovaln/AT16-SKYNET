#
# @success_convert_post.py Copyright (c) 2022 Jalasoft.
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

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SuccessConvertPost(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, status: str=None, message: str=None):  # noqa: E501
        """SuccessConvertPost - a model defined in Swagger

        :param status: The status of this SuccessConvertPost.  # noqa: E501
        :type status: str
        :param message: The message of this SuccessConvertPost.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'status': str,
            'message': str
        }

        self.attribute_map = {
            'status': 'status',
            'message': 'message'
        }

        self._status = status
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'SuccessConvertPost':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SuccessConvertPost of this SuccessConvertPost.  # noqa: E501
        :rtype: SuccessConvertPost
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self) -> str:
        """Gets the status of this SuccessConvertPost.


        :return: The status of this SuccessConvertPost.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this SuccessConvertPost.


        :param status: The status of this SuccessConvertPost.
        :type status: str
        """

        self._status = status

    @property
    def message(self) -> str:
        """Gets the message of this SuccessConvertPost.


        :return: The message of this SuccessConvertPost.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this SuccessConvertPost.


        :param message: The message of this SuccessConvertPost.
        :type message: str
        """

        self._message = message
