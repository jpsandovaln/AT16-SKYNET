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


class SuccessResult(ResultBooking):
    def __init__(self, status: str, message: str):
        super().__init__(status)
        self.message: str = message

    def get_message(self) -> str:
        return self.message