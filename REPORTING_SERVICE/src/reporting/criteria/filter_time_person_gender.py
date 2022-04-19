#
# @filters_time_person_gender.py Copyright (c)
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

from REPORTING_SERVICE.src.reporting.criteria.criteria import Criteria



class Filters_Start_Finish_Time_Person_Gender:
    def __init__(self, start_time, finish_time, person_age):
        self.start_time = start_time
        self.finish_time = finish_time
        self.person_age = person_age

    def filters_start_finish_time_person_gender(self):
        filters = (Criteria.get_df()["start_time"] >= self.start_time) & \
                  (Criteria.get_df()["end_time"] <= self.finish_time)\
                  & (Criteria.get_df()["person_age"] >= self.person_age)
        return filters




