#
# @change_mongo_pandas.py Copyright (c) 2022 Jalasoft
# 2643 Av Melchor Perez de Olguin , Colquiri Sud, Cochabamba, Bolivia.
# add direccion de jala la paz>
# All rights reserved
#
# This software is the confidential and proprietary information of
# Jalasoft , Confidential Information "). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft

from pymongo import MongoClient
import pandas as pd
from flask import Flask, request, Response, jsonify

MONGO_HOST = "127.0.0.1"
MONGO_PORT = "27017"
MONGO_DB = "database"
MONGO_USER = "admin"
MONGO_PASS = "pass"
#
# uri = "mongodb://{}:{}@{}:{}/{}?authSource=admin".format(MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT, MONGO_DB)

# uri = 'mongodb://db_mongo/'
# client = MongoClient(uri)
client = MongoClient('localhost', 27018)
db = client['project']

class Mongo_2_pandas():
    # This function extract the data of MongoDB and show in pandas format
    @staticmethod
    def extract_data():
        booking = db['booking']
        person = db['person']
        resource = db['resource']
        data_person = pd.json_normalize(person.find())
        data_resource = pd.json_normalize(resource.find())
        data_booking = pd.json_normalize(booking.find())
        data_reduce = pd.concat([data_booking['schedule.date'], data_booking['schedule.start_time'],
                                data_booking['schedule.end_time'], data_booking['state'],
                                data_resource, data_person], axis=1)
        return data_reduce
