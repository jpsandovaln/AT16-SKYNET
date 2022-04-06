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
from src.reporting.criteria.filter_time_person_gender import Filters_Start_Finish_Time_Person_Gender


class SearchReportStartFinishTimePersonGender:
    def __init__(self, request):
        self.request = request

    def search_report_start_finish_time_person_gender(self):
        if request.method == 'POST':
            file_route = request.form.get('file_route')  # This is for the file, the rest is for converter imagen
            start_time = request.form.get('start_time')
            end_time = request.form.get('end_time')
            person_age = request.form.get('person_age')
            Criteria = Filters_Start_Finish_Time_Person_Gender(int(start_time), int(end_time), int(person_age),
                                                               str(file_route))
        return str(Criteria.get_df()[Criteria.filters_start_finish_time_person_gender()])
