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

from src.reporting.criteria.filters_time_location import FiltersTimeLocation
import json


class SearchReportFilTimeLocation:

    @staticmethod
    def search_report_fil_time_location(parameters):
        # Validates parameters
        parameters.validate()
        start_date = parameters.get_start_date()
        end_date = parameters.get_end_date()
        data_frame = parameters.get_data_frame()

        # Executes the filter
        filters = FiltersTimeLocation(start_date, end_date)
        filter_result = filters.fil_time_location(data_frame)
        result_filter = filter_result.to_json(date_format="iso",
                                              orient="records")
        parsed = json.loads(result_filter)
        return json.dumps(parsed)
