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


booking = select_booking_collection()


class Booking:
    def booking_create(self, str_json):
        inserted_data = booking.insert_one(str_json)

        # Add delete field
        id_inserted = inserted_data.inserted_id
        result = inserted_booking = booking.find_one_and_update({'_id': id_inserted}, {'$set': {'delete': 0}})

        # Convert ObjectId to string
        result['_id'] = str(result['_id'])

        return result

    def booking_read_all(self):
        # Dictionary that save all results
        all_results = []

        filter = {"delete": 0}
        result = booking.find(filter)

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
            result = {"message": "Not found"}
        return result

    def booking_read_specific_id(self, id_booking):
        id_object = ObjectId(id_booking)
        filter = {"delete": 0}
        result = booking.find_one({"_id": id_object}, filter)

        if result:
            # Convert ObjectId to string
            result['_id'] = str(result['_id'])
        else:
            result = {"message": "Not found"}
        return result

    def booking_update(self, id_booking, str_json):
        id_object = ObjectId(id_booking)
        result = booking.find_one_and_update({'_id': id_object}, {'$set': str_json},
                                             return_document=ReturnDocument.AFTER)

        if result:
            # Convert ObjectId to string
            result['_id'] = str(result['_id'])
        else:
            result = {"message": "Not found"}
        return result

    def booking_delete(self, id_booking):
        id_object = ObjectId(id_booking)
        result = booking.find_one_and_update({'_id': id_object}, {'$set': {'delete': 1}},
                                             return_document=ReturnDocument.AFTER)

        if result:
            # Convert ObjectId to string
            result['_id'] = str(result['_id'])
        else:
            result = {"message": "Not found"}
        return result
