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

class SearchReportSubjectState:
    def __init__(self, request):
        self.request = request

    def search_report_subject_state(self):
        if request.method == 'POST':
            file_route = request.form.get('file_route')  # This is for the file, the rest is for converter imagen
            subject = request.form.get('subject')
            state = request.form.get('state')
            Criteria = Filters_Subject_State(str(subject), str(state), str(file_route))
        return str(Criteria.get_df()[Criteria.filters_subject_state()])
