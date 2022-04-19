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
import json

from flask import request
<<<<<<< Updated upstream
from REPORTING_SERVICE.src.reporting.criteria.filter_time_person_gender import Filters_Start_Finish_Time_Person_Gender
import json
from REPORTING_SERVICE.src.reporting.criteria.criteria import Criteria


=======
from src.reporting.criteria.filter_time_person_gender import Filters_Start_Finish_Time_Person_Gender
from flask import Response
from src.controller.results.error_result import ErrorResult
from src.controller.results.success_result import SuccessResult
from src.common.exceptions.reporting_exception import ReportingException
from http import HTTPStatus
>>>>>>> Stashed changes
class SearchReportStartFinishTimePersonGender:
    def __init__(self, request):
        self.request = request

    def search_report_start_finish_time_person_gender(self):
<<<<<<< Updated upstream
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

=======

            if request.method == 'POST':
                file_route = request.form.get('file_route')  # This is for the file, the rest is for converter imagen
                start_time = request.form.get('start_time')
                end_time = request.form.get('end_time')
                person_age = request.form.get('person_age')
                Criteria = Filters_Start_Finish_Time_Person_Gender(int(start_time), int(end_time), int(person_age),
                                                               str(file_route))
                result = SuccessResult(HTTPStatus.OK, str(Criteria.get_df()[Criteria.filters_start_finish_time_person_gender()]))

            return Response(
                    json.dump(result.__dict__),
                    status=HTTPStatus.OK,
                    mimetypes='aplication/json'
                )
>>>>>>> Stashed changes
