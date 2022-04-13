#
# @video_converter.py Copyright (c) 2022 Jalasoft
# 2643 Av Melchor Perez de Olguin , Colquiri Sud, Cochabamba, Bolivia.
# add direccion de jala la paz>
# All rights reserved
#
# This software is the confidential and proprietary information of
# Jalasoft , Confidential Information "). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft

#from BOOKING_SERVICE.src.model.resource import Resource
#from BOOKING_SERVICE.src.model.person import Person
#from BOOKING_SERVICE.src.model.booking import Booking
from BOOKING_SERVICE.src.model.data_base_collections import *
import pandas as pd
from pymongo import MongoClient, ReturnDocument
object_valueP = {
                'person_full_name': 'Rodrigo',
                'person_age': 34,
                'person_country': 'Brasil',
                'person_city': 'Brasilia',
                'person_gender': 'Masculino',
               }
object_valueR = {
                'name': 'DVD',
                'type': '3D',
                'model': 'Phil2022',
                'state': 'free',
               }
object_valueB = {
                'details': {'subject':'sujeto', 'description': 'descripcion'},
                'schedule': {'date':'hoy', 'start_time': '0:00', 'end_time': '1:00'},
                'state': 'negro',
                'type': 'hoja',
                'resource': {'id': 'coment'},
                'person': {'id': 'manuel'}
               }
person = select_person_collection()
# person.insert_one(object_valueP)
# person.find_one_and_delete({'person_gender': 'person_gender'})
resource = select_resource_collection()
# resource.insert_one(object_valueR)
# resource.find_one_and_delete({'state': 'free'})
booking = select_booking_collection()
# booking.insert_one(object_valueB)
resultP = person.find()
resultR = resource.find()
resultB = booking.find()
dataP = pd.DataFrame(list(resultP))
dataR = pd.DataFrame(list(resultR))
dataB = pd.DataFrame(list(resultB))
dataReduce = pd.concat([dataP['person_full_name'],dataP['person_age'], dataR['name'],
                       dataB['type']], axis=1)
print(dataReduce)