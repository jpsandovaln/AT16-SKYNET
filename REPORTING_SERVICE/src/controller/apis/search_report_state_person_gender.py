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

from src.reporting.criteria.filters_state_person_gender import FiltersStatePersonGender
import json


class SearchReportStatePersonGender:
    @staticmethod
    def search_report_state_person_gender(parameters) -> dict:
        # Validates parameters
        parameters.validate()
        person_gender: parameters = parameters.get_person_gender()
        state: parameters = parameters.get_state()
        data_frame: parameters = parameters.get_data_frame()

        # Execute the filter
        filters: FiltersStatePersonGender = FiltersStatePersonGender(str(state), str(person_gender))
        filter_result: bool = filters.filters_state_person_gender(data_frame)
        filter_rows: any = (data_frame[filter_result])
        result: any = filter_rows.to_json(date_format="iso", orient="records")
        parsed: any = json.loads(result)
        return json.dumps(parsed)
