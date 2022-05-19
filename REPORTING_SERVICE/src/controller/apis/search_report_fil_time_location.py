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
        start_time: parameters = parameters.get_start_time()
        end_time: parameters = parameters.get_end_time()
        location: parameters = parameters.get_location()
        data_frame: parameters = parameters.get_data_frame()

        # Executes the filter
        filters: FiltersTimeLocation = FiltersTimeLocation(start_time, end_time, str(location))
        filter_result: bool = filters.fil_time_location(data_frame)
        filter_rows: any = (data_frame[filter_result])
        result_filter: any = filter_rows.to_json(date_format="iso",
                                            orient="records")
        parsed: any = json.loads(result_filter)
        return json.dumps(parsed)
