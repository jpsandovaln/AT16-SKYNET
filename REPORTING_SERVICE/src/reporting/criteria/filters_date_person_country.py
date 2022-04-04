#
# @filters_date_person_country.py Copyright (c)
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


class Filters_Date_Person_Country(Criteria):
    def __init__(self, date, person_country, direction):
        super().__init__(direction)
        self.date = date
        self.person_country = person_country

    def filters_date_person_country(self):
        filters = (self.get_df()["date"] <= self.date) & (self.get_df()["person_country"] == self.person_country)
        return filters
