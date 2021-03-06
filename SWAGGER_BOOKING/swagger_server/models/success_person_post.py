#
# @success_person_post.py Copyright (c) 2022 Jalasoft.
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


class SuccessPersonPost(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, person_full_name: str=None, person_age: int=None, person_country: str=None, person_city: str=None, person_gender: str=None):  # noqa: E501
        """SuccessPersonPost - a model defined in Swagger

        :param id: The id of this SuccessPersonPost.  # noqa: E501
        :type id: str
        :param person_full_name: The person_full_name of this SuccessPersonPost.  # noqa: E501
        :type person_full_name: str
        :param person_age: The person_age of this SuccessPersonPost.  # noqa: E501
        :type person_age: int
        :param person_country: The person_country of this SuccessPersonPost.  # noqa: E501
        :type person_country: str
        :param person_city: The person_city of this SuccessPersonPost.  # noqa: E501
        :type person_city: str
        :param person_gender: The person_gender of this SuccessPersonPost.  # noqa: E501
        :type person_gender: str
        """
        self.swagger_types = {
            'id': str,
            'person_full_name': str,
            'person_age': int,
            'person_country': str,
            'person_city': str,
            'person_gender': str
        }

        self.attribute_map = {
            'id': '_id',
            'person_full_name': 'person_full_name',
            'person_age': 'person_age',
            'person_country': 'person_country',
            'person_city': 'person_city',
            'person_gender': 'person_gender'
        }

        self._id = id
        self._person_full_name = person_full_name
        self._person_age = person_age
        self._person_country = person_country
        self._person_city = person_city
        self._person_gender = person_gender

    @classmethod
    def from_dict(cls, dikt) -> 'SuccessPersonPost':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SuccessPersonPost of this SuccessPersonPost.  # noqa: E501
        :rtype: SuccessPersonPost
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this SuccessPersonPost.

        ID Person  # noqa: E501

        :return: The id of this SuccessPersonPost.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this SuccessPersonPost.

        ID Person  # noqa: E501

        :param id: The id of this SuccessPersonPost.
        :type id: str
        """

        self._id = id

    @property
    def person_full_name(self) -> str:
        """Gets the person_full_name of this SuccessPersonPost.

        Full name  # noqa: E501

        :return: The person_full_name of this SuccessPersonPost.
        :rtype: str
        """
        return self._person_full_name

    @person_full_name.setter
    def person_full_name(self, person_full_name: str):
        """Sets the person_full_name of this SuccessPersonPost.

        Full name  # noqa: E501

        :param person_full_name: The person_full_name of this SuccessPersonPost.
        :type person_full_name: str
        """

        self._person_full_name = person_full_name

    @property
    def person_age(self) -> int:
        """Gets the person_age of this SuccessPersonPost.

        Age  # noqa: E501

        :return: The person_age of this SuccessPersonPost.
        :rtype: int
        """
        return self._person_age

    @person_age.setter
    def person_age(self, person_age: int):
        """Sets the person_age of this SuccessPersonPost.

        Age  # noqa: E501

        :param person_age: The person_age of this SuccessPersonPost.
        :type person_age: int
        """

        self._person_age = person_age

    @property
    def person_country(self) -> str:
        """Gets the person_country of this SuccessPersonPost.

        Country  # noqa: E501

        :return: The person_country of this SuccessPersonPost.
        :rtype: str
        """
        return self._person_country

    @person_country.setter
    def person_country(self, person_country: str):
        """Sets the person_country of this SuccessPersonPost.

        Country  # noqa: E501

        :param person_country: The person_country of this SuccessPersonPost.
        :type person_country: str
        """

        self._person_country = person_country

    @property
    def person_city(self) -> str:
        """Gets the person_city of this SuccessPersonPost.

        City  # noqa: E501

        :return: The person_city of this SuccessPersonPost.
        :rtype: str
        """
        return self._person_city

    @person_city.setter
    def person_city(self, person_city: str):
        """Sets the person_city of this SuccessPersonPost.

        City  # noqa: E501

        :param person_city: The person_city of this SuccessPersonPost.
        :type person_city: str
        """

        self._person_city = person_city

    @property
    def person_gender(self) -> str:
        """Gets the person_gender of this SuccessPersonPost.

        Gender  # noqa: E501

        :return: The person_gender of this SuccessPersonPost.
        :rtype: str
        """
        return self._person_gender

    @person_gender.setter
    def person_gender(self, person_gender: str):
        """Sets the person_gender of this SuccessPersonPost.

        Gender  # noqa: E501

        :param person_gender: The person_gender of this SuccessPersonPost.
        :type person_gender: str
        """

        self._person_gender = person_gender
