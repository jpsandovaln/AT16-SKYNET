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

from src.reporting.criteria.filters_date_person_country import FiltersDatePersonCountry
import json


class SearchReportDatePersonCountry:

    @staticmethod
    def search_report_date_person_country(parameters) -> dict:
        # Validates parameters
        parameters.validate()
        date: parameters = parameters.get_date()
        person_country: parameters = parameters.get_person_country()
        data_frame: parameters = parameters.get_data_frame()

        # Executes the filter
        filters: FiltersDatePersonCountry = FiltersDatePersonCountry(date, str(person_country))
        filter_result: bool = filters.filters_date_person_country(data_frame)
        filter_rows: any = (data_frame[filter_result])
        result_filter: any = filter_rows.to_json(date_format="iso",
                                            orient="records")
        parsed:any = json.loads(result_filter)
        return json.dumps(parsed)
