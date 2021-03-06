#
# @success_gender_post.py Copyright (c) 2022 Jalasoft.
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
from swagger_server import util


class SuccessGenderPost(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, person_gender: str=None, morning: int=None, afternoon: int=None):  # noqa: E501
        """SuccessGenderPost - a model defined in Swagger

        :param person_gender: The person_gender of this SuccessGenderPost.  # noqa: E501
        :type person_gender: str
        :param morning: The morning of this SuccessGenderPost.  # noqa: E501
        :type morning: int
        :param afternoon: The afternoon of this SuccessGenderPost.  # noqa: E501
        :type afternoon: int
        """
        self.swagger_types = {
            'person_gender': str,
            'morning': int,
            'afternoon': int
        }

        self.attribute_map = {
            'person_gender': 'person_gender',
            'morning': 'morning',
            'afternoon': 'afternoon'
        }

        self._person_gender = person_gender
        self._morning = morning
        self._afternoon = afternoon

    @classmethod
    def from_dict(cls, dikt) -> 'SuccessGenderPost':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SuccessGenderPost of this SuccessGenderPost.  # noqa: E501
        :rtype: SuccessGenderPost
        """
        return util.deserialize_model(dikt, cls)

    @property
    def person_gender(self) -> str:
        """Gets the person_gender of this SuccessGenderPost.


        :return: The person_gender of this SuccessGenderPost.
        :rtype: str
        """
        return self._person_gender

    @person_gender.setter
    def person_gender(self, person_gender: str):
        """Sets the person_gender of this SuccessGenderPost.


        :param person_gender: The person_gender of this SuccessGenderPost.
        :type person_gender: str
        """

        self._person_gender = person_gender

    @property
    def morning(self) -> int:
        """Gets the morning of this SuccessGenderPost.


        :return: The morning of this SuccessGenderPost.
        :rtype: int
        """
        return self._morning

    @morning.setter
    def morning(self, morning: int):
        """Sets the morning of this SuccessGenderPost.


        :param morning: The morning of this SuccessGenderPost.
        :type morning: int
        """

        self._morning = morning

    @property
    def afternoon(self) -> int:
        """Gets the afternoon of this SuccessGenderPost.


        :return: The afternoon of this SuccessGenderPost.
        :rtype: int
        """
        return self._afternoon

    @afternoon.setter
    def afternoon(self, afternoon: int):
        """Sets the afternoon of this SuccessGenderPost.


        :param afternoon: The afternoon of this SuccessGenderPost.
        :type afternoon: int
        """

        self._afternoon = afternoon
