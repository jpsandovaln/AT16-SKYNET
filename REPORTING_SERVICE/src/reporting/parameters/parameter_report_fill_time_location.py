#
# @parameter_report_fil_time_location.py Copyright (c) 2022 Jalasoft.
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


class ParameterReportFillTimeLocation:
    def __init__(self, start_time: str, end_time: str, location: str, data_frame: type):
        self.start_time: str = start_time
        self.end_time: str = end_time
        self.location: str = location
        self.data_frame: type = data_frame

    def get_start_time(self) -> str:
        return self.start_time

    def get_end_time(self) -> str:
        return self.end_time

    def get_location(self) -> str:
        return self.location

    def get_data_frame(self) -> type:
        return self.data_frame

    def validate(self):
        if self.start_time is None or str(self.start_time).strip() == "":
            message: str = "Invalid start time, the value is empty"
            raise ParameterException(message, "401", "AT16-ERR-351")

        if self.end_time is None or str(self.end_time).strip() == "":
            message: str = "Invalid end time, the value is empty"
            raise ParameterException(message, "401", "AT16-ERR-352")

        if self.location is None or str(self.location).strip() == "":
            message: str = "Invalid location, the value is empty"
            raise ParameterException(message, "401", "AT16-ERR-352")

        if self.data_frame is None or type(self.data_frame) != pd.DataFrame:
            message: str = "Invalid dataframe, the value is incorrect"
            raise ParameterException(message, "401", "AT16-ERR-353")
