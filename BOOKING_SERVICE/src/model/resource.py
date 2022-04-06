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


resource = select_resource_collection()


class Resource:
    def resource_create(self, str_json):
        inserted_data = resource.insert_one(str_json)

        # Add delete field
        id_inserted = inserted_data.inserted_id
        result = resource.find_one_and_update({'_id': id_inserted}, {'$set': {'delete': 0}})

        # Convert ObjectId to string
        result['_id'] = str(result['_id'])

        return result

    def resource_read_all(self):
        # Dictionary that save all results
        all_results = []

        filter = {"delete": 0}
        result = resource.find(filter)

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
            result = {"message": "Not found"}
        return result

    def resource_read_specific_id(self, id_resource):
        id_object = ObjectId(id_resource)
        filter = {"delete": 0}
        result = resource.find_one({"_id": id_object}, filter)

        if result:
            # Convert ObjectId to string
            result['_id'] = str(result['_id'])
        else:
            result = {"message": "Not found"}
        return result

    def resource_update(self, id_resource, str_json):
        id_object = ObjectId(id_resource)
        result = resource.find_one_and_update({'_id': id_object}, {'$set': str_json},
                                              return_document=ReturnDocument.AFTER)

        if result:
            # Convert ObjectId to string
            result['_id'] = str(result['_id'])
        else:
            result = {"message": "Not found"}
        return result

    def resource_delete(self, id_resource):
        id_object = ObjectId(id_resource)
        result = resource.find_one_and_update({'_id': id_object}, {'$set': {'delete': 1}},
                                              return_document=ReturnDocument.AFTER)

        if result:
            # Convert ObjectId to string
            result['_id'] = str(result['_id'])
        else:
            result = {"message": "Not found"}
        return result
