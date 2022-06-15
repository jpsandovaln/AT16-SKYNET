#
# @parameter_report_time_person_gender.py Copyright (c) 2022 Jalasoft.
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


class ParameterReportTimePersonGender:
    def __init__(self, open_time: str, close_time: str, data_frame: type):
        self.open_time: str = open_time
        self.close_time: str = close_time
        self.data_frame: type = data_frame

    def get_open_time(self) -> str:
        return self.open_time

    def get_close_time(self) -> str:
        return self.close_time

    def get_data_frame(self) -> type:
        return self.data_frame

    def validate(self):
        if self.open_time is None or str(self.open_time).strip() == "":
            message: str = "Invalid open time, the value is empty"
            raise ParameterException(message, "401", "AT16-ERR-351")

        if self.close_time is None or str(self.close_time).strip() == "":
            message: str = "Invalid close time, the value is empty"
            raise ParameterException(message, "401", "AT16-ERR-352")

        if self.data_frame is None or type(self.data_frame) != pd.DataFrame:
            message: str = "Invalid dataframe, the value is incorrect"
            raise ParameterException(message, "401", "AT16-ERR-353")
