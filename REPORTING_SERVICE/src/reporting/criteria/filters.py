#
# @filters.py Copyright (c)
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
from csv import excel
from src.reporting.criteria.criteria import Criteria
import pandas as pd


class Filters(Criteria):
    def __init__(self, star_time, finish_time, location, direction):
        super().__init__(star_time, finish_time, location, direction)

    def fil(self):
        excel = self.direction
        df = pd.read_excel(excel)
        fill = (df['start_time'] >= self.star_time) & (df['end_time'] <= self.finish_time) & (
                df['person_city'] == self.location)
        return df[fill]
