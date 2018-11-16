import inspect
import logging
from datetime import datetime


def logger(log_level=logging.DEBUG):
    # get the name of instance where invoked
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # save log to file
    file_handler = logging.FileHandler('EasyPay_Test_Run_{:%Y-%m-%d}.log'
                                       .format(datetime.now()), mode='a')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - '
                                  '%(levelname)s: %(message)s',
                                  datefmt="%Y-%m-%d %H:%M:%S %p")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
