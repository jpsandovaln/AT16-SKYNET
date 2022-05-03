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

from flask import request, jsonify
import json
from src.reporting.criteria.criteria import Criteria
from src.reporting.criteria.filter_time_person_gender import Filters_Start_Finish_Time_Person_Gender


class SearchReportStartFinishTimePersonGender:
    def __init__(self, request):
        self.request = request

    def search_report_start_finish_time_person_gender(self):

        if request.method == 'POST':
            start_time = request.form.get('start_time')
            end_time = request.form.get('end_time')
            person_age = request.form.get('person_age')
            filters = Filters_Start_Finish_Time_Person_Gender(int(start_time),
                                                              int(end_time),
                                                              int(person_age))
            filter_result = filters.filters_start_finish_time_person_gender()
        filter_rows = (Criteria.get_df()[filter_result])
        result = filter_rows.to_json(date_format="iso", orient="records")
        parsed = json.loads(result)
        return json.dumps(parsed, indent=4)
