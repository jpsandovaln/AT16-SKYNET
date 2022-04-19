#
# @resource.py Copyright (c)
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
from .data_base_collections import select_resource_collection
from bson.objectid import ObjectId
from src.common.exceptions.booking_exception import BookingException

resource = select_resource_collection()


class Resource:
    def resource_create(self, str_json):
        inserted_data = resource.insert_one(str_json)

        # Add delete field
        id_inserted = inserted_data.inserted_id
        result = resource.find_one_and_update({'_id': id_inserted}, {'$set': {'delete': 0}})

        if result is None or result == "":
            raise BookingException("Error insert in data base", "601", "AT16-ERROR-100", "resource_create")
        # Convert ObjectId to string
        result['_id'] = str(result['_id'])

        return result

    def resource_read_all(self):
        # Dictionary that save all results
        all_results = []

        filter = {"delete": 0}
        result = resource.find(filter)

        if result is None or result == "":
            raise BookingException("Error read in data base", "602", "AT16-ERROR-101", "resource_read_all")
        # Fill the dictionary
        for result_by_element in result:
            result_by_element['_id'] = str(result_by_element['_id'])
            all_results.append(result_by_element)

        return all_results

    def resource_read_specific_name(self, name):
        filter = {"delete": 0}
        result = resource.find_one(name, filter)

        if result:
            # Convert ObjectId to string
            result['_id'] = str(result['_id'])
        else:
            raise BookingException("Invalid specific name", "603", "AT16-ERROR-105", "resource_read_specific_name")
        return result

    def resource_read_specific_id(self, id_resource):
        id_object = ObjectId(id_resource)
        filter = {"delete": 0}
        result = resource.find_one({"_id": id_object}, filter)

        if result:
            # Convert ObjectId to string
            result['_id'] = str(result['_id'])
        else:
            raise BookingException("Invalid specific ID", "603", "AT16-ERROR-106", "resource_read_specific_id")
        return result

    def resource_update(self, id_resource, str_json):
        id_object = ObjectId(id_resource)
        result = resource.find_one_and_update({'_id': id_object}, {'$set': str_json},
                                              return_document=ReturnDocument.AFTER)

        if result:
            # Convert ObjectId to string
            result['_id'] = str(result['_id'])
        else:
            raise BookingException("Can not be update", "606", "AT16-ERROR-107", "resource_update")
        return result

    def resource_delete(self, id_resource):
        id_object = ObjectId(id_resource)
        result = resource.find_one_and_update({'_id': id_object}, {'$set': {'delete': 1}},
                                              return_document=ReturnDocument.AFTER)

        if result:
            # Convert ObjectId to string
            result['_id'] = str(result['_id'])
        else:
            raise BookingException("Can not be delete", "608", "AT16-ERROR-108", "resource_delete")
        return result
