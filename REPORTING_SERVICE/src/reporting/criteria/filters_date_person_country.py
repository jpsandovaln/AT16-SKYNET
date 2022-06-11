#
# @filters_date_person_country.py Copyright (c)
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

from datetime import datetime


class FiltersDatePersonCountry:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def filters_date_person_country(self, data_frame):
        end_date = datetime.strptime(self.end_date, '%m/%d/%Y').date()
        start_date = datetime.strptime(self.start_date, '%m/%d/%Y').date()
        filters_date = (data_frame["date"] >= start_date) & (data_frame["date"] <= end_date)
        df_date = data_frame[filters_date]
        result_graphs = df_date.groupby(['person_country']).size().reset_index(
            name='quantity')
        return result_graphs
