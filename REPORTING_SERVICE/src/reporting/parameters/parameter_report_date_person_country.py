#
# @parameter_report_date_person_country.py Copyright (c) 2022 Jalasoft.
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


class ParameterReportDatePersonCountry:
    def __init__(self, date: str, person_country: str, data_frame: type):
        self.date: str = date
        self.person_country: str = person_country
        self.data_frame: type = data_frame

    def get_date(self) -> str:
        return self.date

    def get_person_country(self) -> str:
        return self.person_country

    def get_data_frame(self) -> type:
        return self.data_frame

    def validate(self):
        if self.date is None or str(self.date).strip() == "":
            message: str = "Invalid date, the value is empty"
            raise ParameterException(message, "401", "AT16-ERR-351")

        if self.person_country is None or str(self.person_country).strip() == "":
            message: str = "Invalid country, the value is empty"
            raise ParameterException(message, "401", "AT16-ERR-352")

        if self.data_frame is None or type(self.data_frame) != pd.DataFrame:
            message: str = "Invalid dataframe, the value is incorrect"
            raise ParameterException(message, "401", "AT16-ERR-353")
