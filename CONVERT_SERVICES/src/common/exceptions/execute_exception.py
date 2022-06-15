#
# @execute_exception.py Copyright (c)
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

from src.common.exceptions.convert_services_exception import ConvertServicesException


class ExecuteException(ConvertServicesException):
    def __init__(self, message: str, status: str, code: str):
        super().__init__(message, status, code)
