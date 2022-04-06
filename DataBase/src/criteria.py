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

class Criteria:
    def __init__(self, star_time, finish_time, location, direction):
        self.star_time = star_time
        self.finish_time = finish_time
        self.location = location
        self.direction = direction

    def get_star_time(self):
        return self.star_time

    def get_finish_time(self):
        return self.finish_time

    def get_location(self):
        return self.location

    def get_direction(self):
        return self.direction
