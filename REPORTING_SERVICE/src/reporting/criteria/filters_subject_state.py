#
# @filters_subject_state.py Copyright (c)
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

from src.reporting.criteria.criteria import Criteria


class Filters_Subject_State(Criteria):
    def __init__(self, subject, state, direction):
        super().__init__(direction)
        self.subject = subject
        self.state = state

    def filters_subject_state(self):
        filters = (self.get_df()["subject"] == self.subject) & (self.get_df()["state"] == self.state)
        return filters





