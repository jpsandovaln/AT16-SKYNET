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

from models.data_base_collections import select_person_collection
from bson.objectid import ObjectId


person = select_person_collection()


class Person:
    def person_create(self, str_json):
        inserted_data = person.insert_one(str_json)

        #If need add delete field
        id_inserted = inserted_data.inserted_id
        person.find_one_and_update({'_id': id_inserted}, {'$set': {'delete': 0}})

    def person_read_all(self):
        filter = {"delete": 0}
        result = person.find(filter)
        for result_by_element in result:
            print(result_by_element)

    def person_read_specific_name(self, name):
        filter = {"delete": 0}
        result = person.find_one(name, filter)
        print(result)

    def person_read_specific_id(self, id_person):
        id_object = ObjectId(id_person)
        filter = {"delete": 0}
        print(person.find_one({"_id": id_object}, filter))

    def person_update(self, id_person, str_json):
        id_object = ObjectId(id_person)
        person.find_one_and_update({'_id': id_object}, {'$set': str_json})
        print("Update!")

    def person_delete(self, id_person):
        id_object = ObjectId(id_person)
        person.find_one_and_update({'_id': id_object}, {'$set': {'delete': 1}})
        print("Soft delete!")
