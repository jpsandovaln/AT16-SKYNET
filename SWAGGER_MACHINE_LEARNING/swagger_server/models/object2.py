#
# @object2.py Copyright (c) 2022 Jalasoft.
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


class Object2(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, the_person_appears_in: str=None):  # noqa: E501
        """Object2 - a model defined in Swagger

        :param the_person_appears_in: The the_person_appears_in of this Object2.  # noqa: E501
        :type the_person_appears_in: str
        """
        self.swagger_types = {
            'the_person_appears_in': str
        }

        self.attribute_map = {
            'the_person_appears_in': 'The person appears in'
        }

        self._the_person_appears_in = the_person_appears_in

    @classmethod
    def from_dict(cls, dikt) -> 'Object2':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Object2 of this Object2.  # noqa: E501
        :rtype: Object2
        """
        return util.deserialize_model(dikt, cls)

    @property
    def the_person_appears_in(self) -> str:
        """Gets the the_person_appears_in of this Object2.


        :return: The the_person_appears_in of this Object2.
        :rtype: str
        """
        return self._the_person_appears_in

    @the_person_appears_in.setter
    def the_person_appears_in(self, the_person_appears_in: str):
        """Sets the the_person_appears_in of this Object2.


        :param the_person_appears_in: The the_person_appears_in of this Object2.
        :type the_person_appears_in: str
        """

        self._the_person_appears_in = the_person_appears_in
