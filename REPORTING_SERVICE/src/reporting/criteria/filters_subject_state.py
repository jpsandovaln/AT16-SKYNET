#
# @filters_subject_state.py Copyright (c)
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
from src.reporting.criteria.criteria import Criteria
from src.common.exceptions.filter_exception import FilterException


class Filters_Subject_State:
    def __init__(self, subject, state):
        self.subject = subject
        self.state = state

    def filters_subject_state(self):
        Criteria.validate_criteria()
        filters = (Criteria.get_df()["subject"] == self.subject) & \
                  (Criteria.get_df()["state"] == self.state)
        if filters is None or filters == "":
            raise FilterException("Invalid Filter, the value is empty", "101", "AT16-ERROR-101",
                                  "Filters_Start_Finish_Time_Person_Age")
        else:
            return filters





