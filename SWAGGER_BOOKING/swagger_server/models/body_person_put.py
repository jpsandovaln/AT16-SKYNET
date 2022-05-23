#
# @body_person_put.py Copyright (c) 2022 Jalasoft.
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


class BodyPersonPut(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, person_full_name: str=None, person_age: int=None, person_country: str=None, person_city: str=None, person_gender: str=None):  # noqa: E501
        """BodyPersonPut - a model defined in Swagger

        :param person_full_name: The person_full_name of this BodyPersonPut.  # noqa: E501
        :type person_full_name: str
        :param person_age: The person_age of this BodyPersonPut.  # noqa: E501
        :type person_age: int
        :param person_country: The person_country of this BodyPersonPut.  # noqa: E501
        :type person_country: str
        :param person_city: The person_city of this BodyPersonPut.  # noqa: E501
        :type person_city: str
        :param person_gender: The person_gender of this BodyPersonPut.  # noqa: E501
        :type person_gender: str
        """
        self.swagger_types = {
            'person_full_name': str,
            'person_age': int,
            'person_country': str,
            'person_city': str,
            'person_gender': str
        }

        self.attribute_map = {
            'person_full_name': 'person_full_name',
            'person_age': 'person_age',
            'person_country': 'person_country',
            'person_city': 'person_city',
            'person_gender': 'person_gender'
        }

        self._person_full_name = person_full_name
        self._person_age = person_age
        self._person_country = person_country
        self._person_city = person_city
        self._person_gender = person_gender

    @classmethod
    def from_dict(cls, dikt) -> 'BodyPersonPut':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BodyPersonPut of this BodyPersonPut.  # noqa: E501
        :rtype: BodyPersonPut
        """
        return util.deserialize_model(dikt, cls)

    @property
    def person_full_name(self) -> str:
        """Gets the person_full_name of this BodyPersonPut.

        Full name  # noqa: E501

        :return: The person_full_name of this BodyPersonPut.
        :rtype: str
        """
        return self._person_full_name

    @person_full_name.setter
    def person_full_name(self, person_full_name: str):
        """Sets the person_full_name of this BodyPersonPut.

        Full name  # noqa: E501

        :param person_full_name: The person_full_name of this BodyPersonPut.
        :type person_full_name: str
        """

        self._person_full_name = person_full_name

    @property
    def person_age(self) -> int:
        """Gets the person_age of this BodyPersonPut.

        Age  # noqa: E501

        :return: The person_age of this BodyPersonPut.
        :rtype: int
        """
        return self._person_age

    @person_age.setter
    def person_age(self, person_age: int):
        """Sets the person_age of this BodyPersonPut.

        Age  # noqa: E501

        :param person_age: The person_age of this BodyPersonPut.
        :type person_age: int
        """

        self._person_age = person_age

    @property
    def person_country(self) -> str:
        """Gets the person_country of this BodyPersonPut.

        Country  # noqa: E501

        :return: The person_country of this BodyPersonPut.
        :rtype: str
        """
        return self._person_country

    @person_country.setter
    def person_country(self, person_country: str):
        """Sets the person_country of this BodyPersonPut.

        Country  # noqa: E501

        :param person_country: The person_country of this BodyPersonPut.
        :type person_country: str
        """

        self._person_country = person_country

    @property
    def person_city(self) -> str:
        """Gets the person_city of this BodyPersonPut.

        City  # noqa: E501

        :return: The person_city of this BodyPersonPut.
        :rtype: str
        """
        return self._person_city

    @person_city.setter
    def person_city(self, person_city: str):
        """Sets the person_city of this BodyPersonPut.

        City  # noqa: E501

        :param person_city: The person_city of this BodyPersonPut.
        :type person_city: str
        """

        self._person_city = person_city

    @property
    def person_gender(self) -> str:
        """Gets the person_gender of this BodyPersonPut.

        Gender  # noqa: E501

        :return: The person_gender of this BodyPersonPut.
        :rtype: str
        """
        return self._person_gender

    @person_gender.setter
    def person_gender(self, person_gender: str):
        """Sets the person_gender of this BodyPersonPut.

        Gender  # noqa: E501

        :param person_gender: The person_gender of this BodyPersonPut.
        :type person_gender: str
        """

        self._person_gender = person_gender