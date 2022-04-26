#
# @filters_time_location.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from src.reporting.criteria.criteria import Criteria
from src.common.exceptions.filter_exception import FilterException


class Filters_Time_Location:
    def __init__(self, start_time, finish_time, location):
        self.start_time = start_time
        self.finish_time = finish_time
        self.location = location

    def fil_time_location(self):
        Criteria.validate_criteria()
        filters = (Criteria.get_df()['start_time'] >= self.start_time) & \
                  (Criteria.get_df()['end_time'] <= self.finish_time) & \
                  (Criteria.get_df()['person_city'] == self.location)
        if filters is None or filters == "":
            raise FilterException("Invalid Filter, the value is empty", "101", "AT16-ERROR-101",
                                  "Filters_Start_Finish_Time_Person_Age")
        else:
            return filters
