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

from BOOKING_SERVICE.src.model.data_base_collections import *
import pandas as pd

class Mongo_2_pandas():
    # This function extract the data of MongoDB and show in pandas format
    def extract_data(self):
        person = select_person_collection()
        resource = select_resource_collection()
        booking = select_booking_collection()
        dataP = pd.DataFrame(list(person.find()))
        dataR = pd.DataFrame(list(resource.find()))
        dataB = pd.json_normalize(booking.find())
        dataReduce = pd.concat([dataB['schedule.date'], dataB['schedule.start_time'],
                                dataB['schedule.end_time'], dataB['state'], dataR,
                                dataP], axis=1)
        return dataReduce
