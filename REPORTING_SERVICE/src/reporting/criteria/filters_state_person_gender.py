#
# @filters_state_person_gender.py Copyright (c)
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

class FiltersStatePersonGender:
    def __init__(self, state: str, person_gender: str):
        self.state: str = state
        self.person_gender: str = person_gender

    def filters_state_person_gender(self, data_frame: type) -> bool:
        filters: bool = (data_frame["state"] == self.state) & \
          (data_frame["person_gender"] == self.person_gender)
        return filters
