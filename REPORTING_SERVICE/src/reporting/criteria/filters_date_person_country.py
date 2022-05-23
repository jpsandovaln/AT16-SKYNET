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
import time
from datetime import datetime


class FiltersDatePersonCountry:
    def __init__(self, date: str, person_country: str):
        self.date: str = date
        self.person_country: str = person_country

    def filters_date_person_country(self, data_frame) -> bool:
        date_time: time = datetime.strptime(self.date, '%m/%d/%Y').date()
        filters: bool = (data_frame["date"] <= date_time) & \
                        (data_frame["person_country"] == self.person_country)
        return filters
