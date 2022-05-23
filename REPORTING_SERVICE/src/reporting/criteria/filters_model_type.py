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


class FiltersModelType:

    def __init__(self, model: str, resource_type: type):
        self.model: str = model
        self.resource_type: type = resource_type

    def filters_model_type(self, data_frame) ->bool:
        filters: bool = (data_frame["resource_model"] == self.model) & \
                  (data_frame["resource_type"] == self.resource_type)
        return filters
