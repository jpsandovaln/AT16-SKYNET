#
# @filters_time_location.py Copyright (c)
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


class FiltersTimeLocation:

    def __init__(self, start_time, end_time, location):
        self.start_time = start_time
        self.end_time = end_time
        self.location = location

    def fil_time_location(self, data_frame):
        start_time = datetime.strptime(self.start_time, '%H:%M:%S').time()
        end_time = datetime.strptime(self.end_time, '%H:%M:%S').time()
        filters = (data_frame['start_time'] >= start_time) & \
                  (data_frame['end_time'] <= end_time) & \
                  (data_frame['person_city'] == self.location)
        return filters