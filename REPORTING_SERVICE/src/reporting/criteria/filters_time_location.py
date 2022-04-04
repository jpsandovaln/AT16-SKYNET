#
# @filters_time_location.py Copyright (c)
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


from src.reporting.criteria.criteria import Criteria


class Filters_Time_Location(Criteria):
    def __init__(self, star_time, finish_time, location, direction):
        super().__init__(direction)
        self.star_time = star_time
        self.finish_time = finish_time
        self.location = location

    def fil_time_location(self):
        filters = (self.get_df()['start_time'] >= self.star_time) & (self.get_df()['end_time'] <= self.finish_time) & (
                self.get_df()['person_city'] == self.location)
        return filters
