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


class Filters_Subject_State:
    def __init__(self, subject, state):
        self.subject = subject
        self.state = state

    def filters_subject_state(self):
        filters = (Criteria.get_df()["subject"] == self.subject) & \
                  (Criteria.get_df()["state"] == self.state)
        return filters





