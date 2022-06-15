#
# @resource_controller.py Copyright (c) 2022 Jalasoft.
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
from swagger_server.models.body_resource_post import BodyResourcePost  # noqa: E501
from swagger_server.models.body_resource_put import BodyResourcePut  # noqa: E501
from swagger_server.models.success_resource_get import SuccessResourceGet  # noqa: E501
from swagger_server.models.success_resource_id_get import SuccessResourceIdGet  # noqa: E501
from swagger_server.models.success_resource_post import SuccessResourcePost  # noqa: E501
from swagger_server import util


def deleteresource(id_resource):  # noqa: E501
    """Delete a Resource by Id of the Database of Booking

    Delete a resource # noqa: E501

    :param id_resource: Id resource
    :type id_resource: str

    :rtype: SuccessResourceGet
    """
    return 'do some magic!'


def findresource():  # noqa: E501
    """Find a resource

    Find a resource # noqa: E501


    :rtype: SuccessResourceGet
    """
    return 'do some magic!'


def findresourcebyid(id_resource):  # noqa: E501
    """Find a resource by id

    Find a resource by id # noqa: E501

    :param id_resource: Find a resource by id
    :type id_resource: str

    :rtype: SuccessResourceIdGet
    """
    return 'do some magic!'


def findresourcebyname(resource_name):  # noqa: E501
    """Find a resource by name

    Find a resource by name # noqa: E501

    :param resource_name: Resource name
    :type resource_name: str

    :rtype: SuccessResourceIdGet
    """
    return 'do some magic!'


def insertresource(body):  # noqa: E501
    """Insert a resource

     # noqa: E501

    :param body: Insert a resource
    :type body: dict | bytes

    :rtype: SuccessResourcePost
    """
    if connexion.request.is_json:
        body = BodyResourcePost.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def updateresource(id_resource, body):  # noqa: E501
    """Update a Resource by Id

    Update a resource # noqa: E501

    :param id_resource: Id resource
    :type id_resource: str
    :param body: Find a resource
    :type body: dict | bytes

    :rtype: SuccessResourceGet
    """
    if connexion.request.is_json:
        body = BodyResourcePut.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
