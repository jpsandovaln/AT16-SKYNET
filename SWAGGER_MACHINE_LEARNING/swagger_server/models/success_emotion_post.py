# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SuccessEmotionPost(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, status: str=None, message: object=None):  # noqa: E501
        """SuccessEmotionPost - a model defined in Swagger

        :param status: The status of this SuccessEmotionPost.  # noqa: E501
        :type status: str
        :param message: The message of this SuccessEmotionPost.  # noqa: E501
        :type message: object
        """
        self.swagger_types = {
            'status': str,
            'message': object
        }

        self.attribute_map = {
            'status': 'status',
            'message': 'message'
        }

        self._status = status
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'SuccessEmotionPost':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SuccessEmotionPost of this SuccessEmotionPost.  # noqa: E501
        :rtype: SuccessEmotionPost
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self) -> str:
        """Gets the status of this SuccessEmotionPost.


        :return: The status of this SuccessEmotionPost.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this SuccessEmotionPost.


        :param status: The status of this SuccessEmotionPost.
        :type status: str
        """

        self._status = status

    @property
    def message(self) -> object:
        """Gets the message of this SuccessEmotionPost.


        :return: The message of this SuccessEmotionPost.
        :rtype: object
        """
        return self._message

    @message.setter
    def message(self, message: object):
        """Sets the message of this SuccessEmotionPost.


        :param message: The message of this SuccessEmotionPost.
        :type message: object
        """

        self._message = message
