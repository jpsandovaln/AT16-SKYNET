#
# @filter_exception.py Copyright (c) 2022 Jalasoft.
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

from src.common.exceptions.reporting_exception import ReportingException


class FilterException(ReportingException):
    def __init__(self, message: str, status: str, code: str, filter: str):
        self.filter: str = filter
        super().__init__(message, status, code)
