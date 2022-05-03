#
# @parameter_report_age_gender.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# Edificio Union № 1376 Av. General Inofuentes esquina Calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import pandas as pd

from src.common.exceptions.parameter_exception import ParameterException


class ParameterReportAgeGender:
    def __init__(self, person_age, person_gender, data_frame):
        self.person_age = person_age
        self.person_gender = person_gender
        self.data_frame = data_frame

    def get_person_age(self):
        return self.person_age

    def get_person_gender(self):
        return self.person_gender

    def get_data_frame(self):
        return self.data_frame

    def validate(self):
        if self.person_age is None or str(self.person_age).strip() == "":
            message = "Invalid person_age, the value is empty"
            raise ParameterException(message, "401", "AT16-ERR-351")

        if self.person_gender is None or str(self.person_gender).strip() == "":
            print(self.person_gender)
            message = "Invalid person_gender, the value is empty"
            raise ParameterException(message, "401", "AT16-ERR-352")

        if self.data_frame is None or type(self.data_frame) != pd.DataFrame:
            message = "Invalid dataframe, the value is incorrect"
            raise ParameterException(message, "401", "AT16-ERR-353")
