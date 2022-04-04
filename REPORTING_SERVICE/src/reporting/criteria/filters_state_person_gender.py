#
# @filters_state_person_gender.py Copyright (c)
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
from csv import excel
from textwrap import fill

from src.reporting.criteria.criteria import Criteria
import pandas as pd


class Filters_State_Person_Gender(Criteria):
    def __init__(self, state, person_gender, direction):
        super().__init__(direction)
        self.state = state
        self.person_gender = person_gender


    def filters_state_person_gender(self):
        filters = (self.get_df()["state"] == self.state) & (self.get_df()["person_gender"] == self.person_gender)
        return filters
