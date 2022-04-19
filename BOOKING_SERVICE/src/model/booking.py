#
# @booking.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Condidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from pymongo import ReturnDocument
from .data_base_collections import select_booking_collection
from bson.objectid import ObjectId
from src.common.exceptions.booking_exception import BookingException


booking = select_booking_collection()


class Booking:
    def booking_create(self, str_json):
        inserted_data = booking.insert_one(str_json)

        # Add delete field
        id_inserted = inserted_data.inserted_id
        result = inserted_booking = booking.find_one_and_update({'_id': id_inserted}, {'$set': {'delete': 0}})
        if result is None or result == "":
            raise BookingException("Error insert in data base", "601", "AT16-ERROR-100", "booking_create")
        # Convert ObjectId to string
        result['_id'] = str(result['_id'])

        return result

    def booking_read_all(self):
        # Dictionary that save all results
        all_results = []

        filter = {"delete": 0}
        result = booking.find(filter)

        if result is None or result == "":
            raise BookingException("Error read in data base", "602", "AT16-ERROR-101", "booking_read_all")

        # Fill the dictionary
        for result_by_element in result:
            result_by_element['_id'] = str(result_by_element['_id'])
            all_results.append(result_by_element)

        return all_results

    def booking_read_specific_name(self, name):
        filter = {"delete": 0}
        result = booking.find_one(name, filter)

        if result:
            # Convert ObjectId to string
            result['_id'] = str(result['_id'])
        else:
            raise BookingException("Invalid specific name", "603", "AT16-ERROR-105", "booking_read_specific_name")
        return result

    def booking_read_specific_id(self, id_booking):
        id_object = ObjectId(id_booking)
        filter = {"delete": 0}
        result = booking.find_one({"_id": id_object}, filter)
        if len(id_booking) == 24:
            raise BookingException("Invalid id long", "501", "AT16-ERROR-301", "booking_read_specific_id")

        if result:
            # Convert ObjectId to string
            result['_id'] = str(result['_id'])
        else:
            raise BookingException("Invalid specific ID", "603", "AT16-ERROR-106", "booking_read_specific_id")
        return result

    def booking_update(self, id_booking, str_json):
        id_object = ObjectId(id_booking)
        result = booking.find_one_and_update({'_id': id_object}, {'$set': str_json},
                                             return_document=ReturnDocument.AFTER)

        if result:
            # Convert ObjectId to string
            result['_id'] = str(result['_id'])
        else:
            raise BookingException("Can not be update", "606", "AT16-ERROR-107", "booking_update")
        return result

    def booking_delete(self, id_booking):
        id_object = ObjectId(id_booking)
        result = booking.find_one_and_update({'_id': id_object}, {'$set': {'delete': 1}},
                                             return_document=ReturnDocument.AFTER)

        if result:
            # Convert ObjectId to string
            result['_id'] = str(result['_id'])
        else:
            raise BookingException("Can not be delete", "608", "AT16-ERROR-108", "booking_delete")
        return result
