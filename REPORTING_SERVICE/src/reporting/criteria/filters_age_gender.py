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

class FiltersAgeGender:
    def __init__(self, person_age, person_gender):
        self.person_age = person_age
        self.person_gender = person_gender

    def filters_age_gender(self, data_frame):
        filters = (data_frame["person_age"] < self.person_age) & \
                  (data_frame["person_gender"] == self.person_gender)
        return filters
