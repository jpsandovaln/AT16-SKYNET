#
# @booking.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Condidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
from src.controller.results.result_booking import ResultBooking


class ErrorResult(ResultBooking):
    def __init__(self, status, message, code):
        super().__init__(status)
        self.message = message
        self.code = code

    def get_message(self):
        return self.message

    def get_code(self):
        return self.code