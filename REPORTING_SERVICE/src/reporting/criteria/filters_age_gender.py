#
# @filters_age_gender.py Copyright (c)
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


class Filters_Age_Gender:
    def __init__(self, person_age, person_gender):
        self.person_age = person_age
        self.person_gender = person_gender

    def filters_age_gender(self):
        filters = (Criteria.get_df()["person_age"] < self.person_age) & \
                  (Criteria.get_df()["person_gender"] == self.person_gender)
        return filters
