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
from src.common.exceptions.booking_exception import BookingException

person: any = select_person_collection()


class Person:
    def person_create(self, str_json) -> str:
        inserted_data: any = person.insert_one(str_json)

        # Add delete field
        id_inserted: any = inserted_data.inserted_id
        inserted_person: any = person.find_one_and_update({'_id': id_inserted}, {'$set': {'delete': 0}})
        result: str = inserted_person
        if result is None or result == "":
            raise BookingException("Error insert in data base", "601", "AT16-ERROR-100", "person_create")
        # Convert ObjectId to string
        result['_id']: str = str(result['_id'])

        return result

    def person_read_all(self) -> list:
        # Dictionary that save all results
        all_results: list = []

        filter: dict = {"delete": 0}
        result = person.find(filter)

        if result is None or result == "":
            raise BookingException("Error read in data base", "602", "AT16-ERROR-101", "person_read_all")

        # Fill the dictionary
        for result_by_element in result:
            result_by_element['_id']: str = str(result_by_element['_id'])
            all_results.append(result_by_element)

        return all_results

    def person_read_specific_name(self, name: str) -> str:
        filter: dict = {"delete": 0}
        result: str = person.find_one(name, filter)

        if result:
            # Convert ObjectId to string
            result['_id']: str = str(result['_id'])
        else:
            raise BookingException("Invalid specific name", "603", "AT16-ERROR-105", "person_read_specific_name")
        return result

    def person_read_specific_id(self, id_person):
        id_object = ObjectId(id_person)
        filter = {"delete": 0}
        result = person.find_one({"_id": id_object}, filter)

        if result:
            # Convert ObjectId to string
            result['_id'] = str(result['_id'])
        else:
            raise BookingException("Invalid specific ID", "603", "AT16-ERROR-106", "person_read_specific_id")
        return result

    def person_update(self, id_person: any, str_json: any) -> str:
        id_object: any = ObjectId(id_person)
        result: any = person.find_one_and_update({'_id': id_object}, {'$set': str_json},
                                                 return_document=ReturnDocument.AFTER)

        if result:
            # Convert ObjectId to string
            result['_id']: str = str(result['_id'])
        else:
            raise BookingException("Can not be update", "606", "AT16-ERROR-107", "person_update")
        return result

    def person_delete(self, id_person: any) -> str:
        id_object: any = ObjectId(id_person)
        result: any = person.find_one_and_update({'_id': id_object}, {'$set': {'delete': 1}},
                                            return_document=ReturnDocument.AFTER)

        if result:
            # Convert ObjectId to string
            result['_id']: str = str(result['_id'])
        else:
            raise BookingException("Can not be delete", "608", "AT16-ERROR-108", "person_delete")
        return result
