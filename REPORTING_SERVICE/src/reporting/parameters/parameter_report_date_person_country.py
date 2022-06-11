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
    def __init__(self, start_date, end_date, data_frame):
        self.start_date = start_date
        self.end_date = end_date
        self.data_frame = data_frame

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_data_frame(self):
        return self.data_frame

    def validate(self):
        if self.start_date is None or str(self.start_date).strip() == "":
            message = "Invalid date, the value is empty"
            raise ParameterException(message, "401", "AT16-ERR-351")

        if self.end_date is None or str(self.end_date).strip() == "":
            message = "Invalid date, the value is empty"
            raise ParameterException(message, "401", "AT16-ERR-351")

        if self.data_frame is None or type(self.data_frame) != pd.DataFrame:
            message = "Invalid dataframe, the value is incorrect"
            raise ParameterException(message, "401", "AT16-ERR-353")
