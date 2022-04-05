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

from models.data_base_collections import select_booking_collection
from bson.objectid import ObjectId


class Booking:
    def booking_create(self, str_json):
        booking = select_booking_collection()
        inserted_data = booking.insert_one(str_json)

        #If need add delete field
        id_inserted = inserted_data.inserted_id
        booking.find_one_and_update({'_id': id_inserted}, {'$set': {'delete': 0}})

    def booking_read_all(self):
        booking = select_booking_collection()
        filter = {"delete": 0}
        result = booking.find(filter)
        for result_by_element in result:
            print(result_by_element)

    def booking_read_specific_name(self, name):
        booking = select_booking_collection()
        filter = {"delete": 0}
        result = booking.find_one(name, filter)
        print(result)

    def booking_read_specific_id(self, id_booking):
        booking = select_booking_collection()
        id_object = ObjectId(id_booking)
        filter = {"delete": 0}
        print(booking.find_one({"_id": id_object}, filter))

    def booking_update(self, id_booking, str_json):
        booking = select_booking_collection()
        id_object = ObjectId(id_booking)
        booking.find_one_and_update({'_id': id_object}, {'$set': str_json})
        print("Update!")

    def booking_delete(self, id_booking):
        booking = select_booking_collection()
        id_object = ObjectId(id_booking)
        booking.find_one_and_update({'_id': id_object}, {'$set': {'delete': 1}})
        print("Soft delete!")
