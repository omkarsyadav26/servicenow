#!/usr/bin/env python3
# coding: UTF-8
"""
Configures the standard Python logging system to comply with:
    https://confluence.gravitant.net/display/Eng/Professional+Software+Development+Standards
"""
import logging
import time

EXTRA = {'requestId':'-'}

LOGGER = logging.getLogger(__name__)
LOG_HANDLER = logging.StreamHandler()
TZ = time.tzname
FORMATTER = logging.Formatter('%(asctime)s '+ str(TZ[0]) +' %(levelname)s %(process)d %(processName)s %(thread)d \
%(threadName)s %(requestId)s %(pathname)s %(funcName)s %(lineno)d | %(message)s')

INFO_LEVEL = logging.INFO
DEBUG_LEVEL = logging.DEBUG

LOG_HANDLER.setFormatter(FORMATTER)
LOGGER.setLevel(logging.INFO)
LOGGER.addHandler(LOG_HANDLER)
logging = logging.LoggerAdapter(LOGGER, EXTRA)


def set_level_debug():
    """
    :return:
    """
    LOGGER.setLevel(DEBUG_LEVEL)

def set_level_info():
    """
    :return:
    """
    LOGGER.setLevel(INFO_LEVEL)