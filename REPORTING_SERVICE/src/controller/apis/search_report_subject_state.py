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
from src.reporting.criteria.filters_subject_state import Filters_Subject_State
import json
from src.reporting.criteria.criteria import Criteria


class SearchReportSubjectState:
    def __init__(self, request):
        self.request = request

    def search_report_subject_state(self):
        if request.method == 'POST':
            subject = request.form.get('subject')
            state = request.form.get('state')
            filters = Filters_Subject_State(str(subject), str(state))
            filter_result = filters.filters_subject_state()
        filter_rows = (Criteria.get_df()[filter_result])
        result = filter_rows.to_json(date_format="iso", orient="records")
        parsed = json.loads(result)
        return json.dumps(parsed, indent=4)
