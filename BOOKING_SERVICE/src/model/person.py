#
# @person.py Copyright (c)
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
from .data_base_collections import select_person_collection
from bson.objectid import ObjectId


person = select_person_collection()


class Person:
    def person_create(self, str_json):
        inserted_data = person.insert_one(str_json)

        # Add delete field
        id_inserted = inserted_data.inserted_id
        result = inserted_person = person.find_one_and_update({'_id': id_inserted}, {'$set': {'delete': 0}})

        # Convert ObjectId to string
        result['_id'] = str(result['_id'])

        return result

    def person_read_all(self):
        # Dictionary that save all results
        all_results = []

        filter = {"delete": 0}
        result = person.find(filter)

        # Fill the dictionary
        for result_by_element in result:
            result_by_element['_id'] = str(result_by_element['_id'])
            all_results.append(result_by_element)

        return all_results

    def person_read_specific_name(self, name):
        filter = {"delete": 0}
        result = person.find_one(name, filter)

        if result:
            # Convert ObjectId to string
            result['_id'] = str(result['_id'])
        else:
            result = {"message": "Not found"}
        return result

    def person_read_specific_id(self, id_person):
        id_object = ObjectId(id_person)
        filter = {"delete": 0}
        result = person.find_one({"_id": id_object}, filter)

        if result:
            # Convert ObjectId to string
            result['_id'] = str(result['_id'])
        else:
            result = {"message": "Not found"}
        return result

    def person_update(self, id_person, str_json):
        id_object = ObjectId(id_person)
        result = person.find_one_and_update({'_id': id_object}, {'$set': str_json},
                                            return_document=ReturnDocument.AFTER)

        if result:
            # Convert ObjectId to string
            result['_id'] = str(result['_id'])
        else:
            result = {"message": "Not found"}
        return result

    def person_delete(self, id_person):
        id_object = ObjectId(id_person)
        result = person.find_one_and_update({'_id': id_object}, {'$set': {'delete': 1}},
                                            return_document=ReturnDocument.AFTER)

        if result:
            # Convert ObjectId to string
            result['_id'] = str(result['_id'])
        else:
            result = {"message": "Not found"}
        return result
