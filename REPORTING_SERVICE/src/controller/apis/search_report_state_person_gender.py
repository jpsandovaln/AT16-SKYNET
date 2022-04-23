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
from src.reporting.criteria.filters_state_person_gender import Filters_State_Person_Gender
import json
from src.reporting.criteria.criteria import Criteria


class SearchReportStatePersonGender:
    def __init__(self, request):
        self.request = request

    def search_report_state_person_gender(self):
        if request.method == 'POST':
            state = request.form.get('state')
            person_gender = request.form.get('person_gender')
            filters = Filters_State_Person_Gender(str(state), str(person_gender))
            filter_result = filters.filters_state_person_gender()
        filter_rows = (Criteria.get_df()[filter_result])
        result = filter_rows.to_json(date_format="iso", orient="records")
        parsed = json.loads(result)
        return json.dumps(parsed, indent=4)
