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

from src.reporting.criteria.filters_model_type import FiltersModelType
import json


class SearchReportModelType:

    @staticmethod
    def search_report_model_type(parameters):

        # Validates parameters
        parameters.validate()
        resource_model = parameters.get_resource_model()
        resource_type = parameters.get_resource_type()
        data_frame = parameters.get_data_frame()

        # Executes the filter
        filters = FiltersModelType(str(resource_model), str(resource_type))
        filter_result = filters.filters_model_type(data_frame)
        filter_rows = (data_frame[filter_result])
        result = filter_rows.to_json(date_format="iso", orient="records")
        parsed = json.loads(result)
        return json.dumps(parsed)
