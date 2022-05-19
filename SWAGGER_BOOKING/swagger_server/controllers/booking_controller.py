#
# @booking_controller.py Copyright (c) 2022 Jalasoft.
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
from swagger_server.models.body_booking_post import BodyBookingPost  # noqa: E501
from swagger_server.models.body_booking_put import BodyBookingPut  # noqa: E501
from swagger_server.models.success_booking_get import SuccessBookingGet  # noqa: E501
from swagger_server.models.success_booking_post import SuccessBookingPost  # noqa: E501
from swagger_server import util


def booking_get():  # noqa: E501
    """Get all booking of the DataBase

     # noqa: E501


    :rtype: SuccessBookingGet
    """
    return 'do some magic!'


def booking_id_booking_delete(id_booking):  # noqa: E501
    """Delete a booking of the DataBase

     # noqa: E501

    :param id_booking: Id booking
    :type id_booking: str

    :rtype: SuccessBookingGet
    """
    return 'do some magic!'


def booking_id_booking_put(id_booking, body):  # noqa: E501
    """Update a Booking by Id

     # noqa: E501

    :param id_booking: Id booking
    :type id_booking: str
    :param body: Insert a booking
    :type body: dict | bytes

    :rtype: SuccessBookingGet
    """
    if connexion.request.is_json:
        body = BodyBookingPut.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def booking_id_id_booking_get(id_booking):  # noqa: E501
    """Get a Booking by Id

     # noqa: E501

    :param id_booking: Id booking
    :type id_booking: str

    :rtype: SuccessBookingGet
    """
    return 'do some magic!'


def booking_post(body):  # noqa: E501
    """Create a Booking

     # noqa: E501

    :param body: Insert a booking
    :type body: dict | bytes

    :rtype: SuccessBookingPost
    """
    if connexion.request.is_json:
        body = BodyBookingPost.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
