#
# @parameter_report_model_type.py Copyright (c) 2022 Jalasoft.
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


class ParameterReportModelType:

    def __init__(self, resource_model: str, resource_type: str, data_frame: type):
        self.resource_model: str = resource_model
        self.resource_type: str = resource_type
        self.data_frame: type = data_frame

    def get_resource_model(self) -> str:
        return self.resource_model

    def get_resource_type(self) -> str:
        return self.resource_type

    def get_data_frame(self) -> type:
        return self.data_frame

    def validate(self):
        if self.resource_model is None or str(self.resource_model).strip() == "":
            message: str = "Invalid resource_model, the value is empty"
            raise ParameterException(message, "401", "AT16-ERR-351")

        if self.resource_type is None or str(self.resource_type).strip() == "":
            message: str = "Invalid resource_type, the value is empty"
            raise ParameterException(message, "401", "AT16-ERR-352")

        if self.data_frame is None or type(self.data_frame) != pd.DataFrame:
            message: str = "Invalid data_frame, the value is incorrect"
            raise ParameterException(message, "401", "AT16-ERR-353")
