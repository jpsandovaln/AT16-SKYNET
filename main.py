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

from BOOKING_SERVICE.src.Config_log_Booking.log_config_booking import Log_Config_Booking
from COMPILER_SERVICE.src.Config_log_Compiler.log_config_compiler import Log_Config_Compiler
from CONVERT_SERVICES.src.Config_log_Convert.log_config_convert import Log_Config_Convert
from MACHINE_LEARNING_SERVICE.src.Config_log_Machine_Learning.log_config_machine import Log_Config_Machine
from REPORTING_SERVICE.src.Config_log_Reporting.log_config_reporting import Log_Config_Reporting

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    Log_Config_Booking.logger.setLevel(logging.DEBUG)
    Log_Config_Compiler.logger.setLevel(logging.DEBUG)
    Log_Config_Convert.logger.setLevel(logging.DEBUG)
    Log_Config_Machine.logger.setLevel(logging.DEBUG)
    Log_Config_Reporting.logger.setLevel(logging.DEBUG)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
