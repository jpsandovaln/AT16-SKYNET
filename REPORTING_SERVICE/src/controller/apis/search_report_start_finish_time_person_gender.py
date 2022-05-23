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
from src.reporting.criteria.filter_time_person_gender import FiltersStartFinishTimePersonGender


class SearchReportStartFinishTimePersonGender:
    @staticmethod
    def search_report_start_finish_time_person_gender(parameters) -> dict:
        # Validates parameters
        parameters.validate()
        open_time: parameters = parameters.get_open_time()
        close_time: parameters = parameters.get_close_time()
        data_frame: parameters = parameters.get_data_frame()

        # Executes the filter
        filters: FiltersStartFinishTimePersonGender = FiltersStartFinishTimePersonGender(open_time, close_time)
        filter_result: bool = filters.filters_start_finish_time_person_gender(data_frame)
        result_filter: any = filter_result.to_json(date_format="iso",
                                            orient="records")
        parsed: any = json.loads(result_filter)
        return json.dumps(parsed)
