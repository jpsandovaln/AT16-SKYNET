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
        #If need add delete field
        id_inserted = inserted_data.inserted_id
        resource.find_one_and_update({'_id': id_inserted}, {'$set': {'delete': 0}})
        return inserted_data

    def resource_read_all(self):
        filter = {"delete": 0}
        result = resource.find(filter)
        return result
        # for result_by_element in result:
        #     print(result_by_element)

    def resource_read_specific_name(self, name):
        filter = {"delete": 0}
        result = resource.find_one(name, filter)
        print(result)
        return result

    def resource_read_specific_id(self, id_resource):
        filter = {"delete": 0}
        result = resource.find_one({"_id": id_resource}, filter)
        print(result)
        return result

    def resource_update(self, id_resource, str_json):
        id_object = ObjectId(id_resource)
        result = resource.find_one_and_update({'_id': id_object}, {'$set': str_json},
                                              return_document=ReturnDocument.AFTER)
        return result

    def resource_delete(self, id_resource):
        id_object = ObjectId(id_resource)
        resource.find_one_and_update({'_id': id_object}, {'$set': {'delete': 1}})
