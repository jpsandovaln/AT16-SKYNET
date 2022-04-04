#
# @search_report.py Copyright (c) 2022 Jalasoft.
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

from flask import request
from src.reporting.criteria.filters_time_location import Filters_Time_Location



class SearchReport:
    def __init__(self, request):
        self.request = request

    def search_report(self):
        if request.method == 'POST':
            file_route = request.form.get('file_route')  # This is for the file, the rest is for converter imagen
            star_time = request.form.get('star_time')
            end_time = request.form.get('end_time')
            location = request.form.get('location')
            Criteria = Filters_Time_Location(int(star_time), int(end_time), str(location), file_route)
        #print(Criteria.get_df()[Criteria.fil_time_location()])
        return str(Criteria.get_df()[Criteria.fil_time_location()])
