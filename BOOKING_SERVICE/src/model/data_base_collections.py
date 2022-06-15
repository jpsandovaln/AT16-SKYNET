#
# @data_base_collection.py Copyright (c)
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

from pymongo import MongoClient
from src.common.exceptions.execute_exception import ExecuteException

MONGO_HOST: str = "127.0.0.1"
MONGO_PORT: str  = "27017"
MONGO_DB: str  = "database"
MONGO_USER: str  = "admin"
MONGO_PASS: str  = "pass"

#uri = "mongodb://{}:{}@{}:{}/{}?authSource=admin".format(MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT, MONGO_DB)
#uri = 'mongodb://127.0.0.1:27017/'

uri: str  = 'mongodb://db_mongo/'
client: any = MongoClient(uri)
db: any = client['project']

if uri is None or uri == "":
    raise ExecuteException("Error connection", "700", "AT16-ERROR-200", "uri = 'mongodb://db_mongo/'")

def select_booking_collection() -> dict:
    booking: dict= db['booking']
    return booking


def select_person_collection() -> dict:
    person: dict = db['person']
    return person


def select_resource_collection() -> dict:
    resource: dict = db['resource']
    return resource
