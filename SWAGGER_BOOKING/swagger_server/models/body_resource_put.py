#
# @body_resource_put.py Copyright (c) 2022 Jalasoft.
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


class BodyResourcePut(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, resource_name: str=None, resource_type: str=None, resource_model: str=None, resource_state: str=None):  # noqa: E501
        """BodyResourcePut - a model defined in Swagger

        :param resource_name: The resource_name of this BodyResourcePut.  # noqa: E501
        :type resource_name: str
        :param resource_type: The resource_type of this BodyResourcePut.  # noqa: E501
        :type resource_type: str
        :param resource_model: The resource_model of this BodyResourcePut.  # noqa: E501
        :type resource_model: str
        :param resource_state: The resource_state of this BodyResourcePut.  # noqa: E501
        :type resource_state: str
        """
        self.swagger_types = {
            'resource_name': str,
            'resource_type': str,
            'resource_model': str,
            'resource_state': str
        }

        self.attribute_map = {
            'resource_name': 'resource_name',
            'resource_type': 'resource_type',
            'resource_model': 'resource_model',
            'resource_state': 'resource_state'
        }

        self._resource_name = resource_name
        self._resource_type = resource_type
        self._resource_model = resource_model
        self._resource_state = resource_state

    @classmethod
    def from_dict(cls, dikt) -> 'BodyResourcePut':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BodyResourcePut of this BodyResourcePut.  # noqa: E501
        :rtype: BodyResourcePut
        """
        return util.deserialize_model(dikt, cls)

    @property
    def resource_name(self) -> str:
        """Gets the resource_name of this BodyResourcePut.

        Resource name  # noqa: E501

        :return: The resource_name of this BodyResourcePut.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name: str):
        """Sets the resource_name of this BodyResourcePut.

        Resource name  # noqa: E501

        :param resource_name: The resource_name of this BodyResourcePut.
        :type resource_name: str
        """

        self._resource_name = resource_name

    @property
    def resource_type(self) -> str:
        """Gets the resource_type of this BodyResourcePut.

        Resource type  # noqa: E501

        :return: The resource_type of this BodyResourcePut.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type: str):
        """Sets the resource_type of this BodyResourcePut.

        Resource type  # noqa: E501

        :param resource_type: The resource_type of this BodyResourcePut.
        :type resource_type: str
        """

        self._resource_type = resource_type

    @property
    def resource_model(self) -> str:
        """Gets the resource_model of this BodyResourcePut.

        Resource model  # noqa: E501

        :return: The resource_model of this BodyResourcePut.
        :rtype: str
        """
        return self._resource_model

    @resource_model.setter
    def resource_model(self, resource_model: str):
        """Sets the resource_model of this BodyResourcePut.

        Resource model  # noqa: E501

        :param resource_model: The resource_model of this BodyResourcePut.
        :type resource_model: str
        """

        self._resource_model = resource_model

    @property
    def resource_state(self) -> str:
        """Gets the resource_state of this BodyResourcePut.

        Resource state  # noqa: E501

        :return: The resource_state of this BodyResourcePut.
        :rtype: str
        """
        return self._resource_state

    @resource_state.setter
    def resource_state(self, resource_state: str):
        """Sets the resource_state of this BodyResourcePut.

        Resource state  # noqa: E501

        :param resource_state: The resource_state of this BodyResourcePut.
        :type resource_state: str
        """

        self._resource_state = resource_state