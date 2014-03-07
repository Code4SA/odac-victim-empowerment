import os.path as op
import logging

LOG_LEVEL = logging.DEBUG
LOGGER_NAME = "msg_handler_logger"  # make sure this is not the same as the name of the package to avoid conflicts with Flask's own logger
DEBUG = False  # If this is true, then replies get logged to file, rather than hitting the vumi API.

ONLINE_LAST_MINUTES = 5