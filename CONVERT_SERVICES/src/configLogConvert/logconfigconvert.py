#
# @main.py Copyright (c)
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
import logging.handlers
import datetime
import time
import os


class LogConfigConvert:
    file_path = os.path.join((os.path.dirname(os.path.abspath(__file__))), 'logs')
    name_log = "convert_service"
    LOG_FILENAME = file_path + datetime.datetime.now().strftime("/" + name_log + ".log")
    logger = logging.getLogger('MyLogger')
    logger.setLevel(logging.DEBUG)
    f = logging.Formatter('%(asctime)s - %(levelname)s - %(levelno)s - %(message)s')
    handler = logging.handlers.TimedRotatingFileHandler(filename=LOG_FILENAME,
                                                        when='s', interval=86400, backupCount=100)
    handler.setFormatter(f)
    logger.addHandler(handler)
