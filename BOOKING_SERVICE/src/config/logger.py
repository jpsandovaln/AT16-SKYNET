#
# @logger.py Copyright (c)
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
import logging
import logging.handlers
import datetime
import time
import os


class LogConfigBooking:
    file_path: str = os.path.join((os.path.dirname(os.path.abspath(__file__))), 'logs')
    name_log: str = "booking_service"
    LOG_FILENAME : str= file_path + datetime.datetime.now().strftime("/" + name_log + ".log")
    logger: logging.Logger = logging.getLogger('MyLogger')
    logger.setLevel(logging.DEBUG)
    f: str = logging.Formatter('%(asctime)s - %(levelname)s - %(levelno)s - %(message)s')
    handler: logging.TimedRotatingFileHandler = logging.handlers.TimedRotatingFileHandler(filename=LOG_FILENAME,
                                                        when='s', interval=86400, backupCount=100)
    handler.setFormatter(f)
    logger.addHandler(handler)

    
