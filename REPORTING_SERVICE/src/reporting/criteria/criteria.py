#
# @criteria.py Copyright (c)
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

import pandas as pd


class Criteria:
    def __init__(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

    def get_df(self):
        excel = self.direction
        df = pd.read_excel(excel)
        return df
