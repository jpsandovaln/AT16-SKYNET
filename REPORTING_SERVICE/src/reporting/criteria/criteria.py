#
# @criteria.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Condidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import pandas as pd
import os
from src.common.exceptions.parameter_exception import ParameterException


class Criteria:
    def __init__(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

    def get_df(self):
        excel = self.direction
        df = pd.read_excel(excel)
        return df

    def validate_criteria(self):
        if self.direction is None or self.direction == "":
            raise ParameterException("Invalid direccion, the value is empty", "606", "AT16-ERROR-101")

        is_file = os.path.isfile(self.direction)
        if not is_file:
            raise ParameterException("It is not file", "406", "AT16-ERROR-201")
