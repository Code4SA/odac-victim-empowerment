import os.path as op
import logging

LOG_LEVEL = logging.DEBUG
LOGGER_NAME = "msg_handler_logger"  # make sure this is not the same as the name of the package to avoid conflicts with Flask's own logger
DEBUG = True

SECRET_KEY = "AEORJAEONIAEGCBGKMALMAENFXGOAERGN"

ACCESS_TOKEN = ''
ACCOUNT_KEY = ''
CONVERSATION_KEY = ''


ONLINE_LAST_MINUTES = 5