import logging
import logging.handlers
import datetime
import time
import os


class Log_Config():
    file_path = os.path.join((os.path.dirname(os.path.abspath(__file__))), 'Logs')
    name_log = "compiler_service"
    LOG_FILENAME = file_path + datetime.datetime.now().strftime("/" + name_log + ".log")
    logger = logging.getLogger('MyLogger')
    logger.setLevel(logging.DEBUG)
    f = logging.Formatter('%(asctime)s - %(levelname)s - %(levelno)s - %(message)s')
    handler = logging.handlers.TimedRotatingFileHandler(filename=LOG_FILENAME,
                                                        when='s', interval=86400, backupCount=100)
    handler.setFormatter(f)
    logger.addHandler(handler)
