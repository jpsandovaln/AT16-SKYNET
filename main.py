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
import logging
from BOOKING_SERVICE.src.config.logger import LogConfigBooking
from COMPILER_SERVICE.src.config.logger import LogConfigCompiler
from CONVERT_SERVICES.src.config.logger import LogConfigConvert
from MACHINE_LEARNING_SERVICE.src.config.logger import LogConfigMachine
from REPORTING_SERVICE.src.config.logger import LogConfigReporting

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    LogConfigBooking.logger.setLevel(logging.DEBUG)
    LogConfigCompiler.logger.setLevel(logging.DEBUG)
    LogConfigConvert.logger.setLevel(logging.DEBUG)
    LogConfigMachine.logger.setLevel(logging.DEBUG)
    LogConfigReporting.logger.setLevel(logging.DEBUG)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
