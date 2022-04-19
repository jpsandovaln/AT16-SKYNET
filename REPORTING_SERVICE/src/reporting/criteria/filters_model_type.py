#
# @filters_model_type.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#


from REPORTING_SERVICE.src.reporting.criteria.criteria import Criteria


class Filters_Model_Type:
    def __init__(self, model, type):
        self.model = model
        self.type = type

    def filters_model_type(self):
        filters = (Criteria.get_df()["resource_model"] == self.model) & \
                  (Criteria.get_df()["resource_type"] == self.type)
        return filters
