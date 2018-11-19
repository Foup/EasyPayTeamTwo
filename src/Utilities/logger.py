import inspect
import logging
import os
import time


def logger(log_level=logging.DEBUG):
    # get the name of instance where invoked
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # save log to file
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    logs_directory = '../../logs/'
    file_name = 'EasyPay_Test_Run_%s.log' % timestamp
    relative_filename = logs_directory + file_name
    current_directory = os.path.dirname(__file__)
    destination_file = os.path.join(current_directory, relative_filename)
    destination_directory = os.path.join(current_directory, logs_directory)
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    file_handler = logging.FileHandler(destination_file, mode='a')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - '
                                  '%(levelname)s: %(message)s',
                                  datefmt="%Y-%m-%d %H:%M:%S %p")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
