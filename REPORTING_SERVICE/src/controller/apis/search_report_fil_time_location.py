#
# @search_report_start_finish_time_person_gender.py Copyright (c) 2022 Jalasoft.
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
from REPORTING_SERVICE.src.reporting.criteria.filters_time_location import Filters_Time_Location
import json
from REPORTING_SERVICE.src.reporting.criteria.criteria import Criteria



class SearchReportFilTimeLocation:
    def __init__(self, request):
        self.request = request

    def search_report_fil_time_location(self):
        if request.method == 'POST':
            start_time = request.form.get('start_time')
            end_time = request.form.get('end_time')
            location = request.form.get('location')
            filters = Filters_Time_Location(int(start_time), int(end_time), str(location))
            filter_result = filters.fil_time_location()
        filter_rows = (Criteria.get_df()[filter_result])
        result = filter_rows.to_json(date_format="iso", orient="records")
        parsed = json.loads(result)
        return json.dumps(parsed, indent=4)
