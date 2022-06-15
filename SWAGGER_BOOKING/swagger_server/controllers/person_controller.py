#
# @person_controller.py Copyright (c) 2022 Jalasoft.
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
from swagger_server.models.body_person_post import BodyPersonPost  # noqa: E501
from swagger_server.models.body_person_put import BodyPersonPut  # noqa: E501
from swagger_server.models.success_person_get import SuccessPersonGet  # noqa: E501
from swagger_server.models.success_person_id_get import SuccessPersonIdGet  # noqa: E501
from swagger_server.models.success_person_post import SuccessPersonPost  # noqa: E501
from swagger_server import util


def get_all():  # noqa: E501
    """Get all Persons of the Database of Booking

     # noqa: E501


    :rtype: SuccessPersonGet
    """
    return 'do some magic!'


def person_id_id_person_get(id_person):  # noqa: E501
    """Get a Person by Id of the Database of Booking

     # noqa: E501

    :param id_person: Id person
    :type id_person: str

    :rtype: SuccessPersonIdGet
    """
    return 'do some magic!'


def person_id_person_delete(id_person):  # noqa: E501
    """Delete a Resource by Id of the Database of Booking

     # noqa: E501

    :param id_person: Id person
    :type id_person: str

    :rtype: SuccessPersonGet
    """
    return 'do some magic!'


def person_id_person_put(id_person, body):  # noqa: E501
    """Update a Person by Id of the Database of Booking

     # noqa: E501

    :param id_person: Id person
    :type id_person: str
    :param body: Insert a person
    :type body: dict | bytes

    :rtype: SuccessPersonGet
    """
    if connexion.request.is_json:
        body = BodyPersonPut.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def person_name_person_name_get(person_name):  # noqa: E501
    """Get a Person by Name of the Database of Booking

     # noqa: E501

    :param person_name: Person name
    :type person_name: str

    :rtype: SuccessPersonIdGet
    """
    return 'do some magic!'


def person_post(body):  # noqa: E501
    """Create a Person into the Database of Booking

     # noqa: E501

    :param body: Insert a person
    :type body: dict | bytes

    :rtype: SuccessPersonPost
    """
    if connexion.request.is_json:
        body = BodyPersonPost.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
