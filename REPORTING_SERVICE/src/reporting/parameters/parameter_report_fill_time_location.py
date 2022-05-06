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
    def __init__(self, start_time, end_time, location, data_frame):
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.data_frame = data_frame

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_location(self):
        return self.location

    def get_data_frame(self):
        return self.data_frame

    def validate(self):
        if self.start_time is None or str(self.start_time).strip() == "":
            message = "Invalid start time, the value is empty"
            raise ParameterException(message, "401", "AT16-ERR-351")

        if self.end_time is None or str(self.end_time).strip() == "":
            message = "Invalid end time, the value is empty"
            raise ParameterException(message, "401", "AT16-ERR-352")

        if self.location is None or str(self.location).strip() == "":
            message = "Invalid location, the value is empty"
            raise ParameterException(message, "401", "AT16-ERR-352")

        if self.data_frame is None or type(self.data_frame) != pd.DataFrame:
            message = "Invalid dataframe, the value is incorrect"
            raise ParameterException(message, "401", "AT16-ERR-353")
