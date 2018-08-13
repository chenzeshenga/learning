import logging
import os

from com.chenzeshenga.module02.homework.conf import prop


def logger():
    atm_logger = logging.getLogger()
    atm_logger.setLevel(logging.INFO)
    log_file = os.path.join(prop.BASE_DIR, 'logs', 'atm.log')
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.INFO)
    fh = logging.FileHandler(log_file)
    formatter = logging.Formatter(prop.LOG_FORMAT)
    fh.setFormatter(formatter)
    # ch.setFormatter(formatter)
    atm_logger.addHandler(fh)
    # atm_logger.addHandler(ch)
    return atm_logger
