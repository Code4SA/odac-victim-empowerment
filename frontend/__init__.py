import logging
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config_frontend.py', silent=True)

# load log level from config
LOG_LEVEL = app.config['LOG_LEVEL']
LOGGER_NAME = app.config['LOGGER_NAME']

# create logger for this application
logger = logging.getLogger(LOGGER_NAME)
logger.setLevel(LOG_LEVEL)

# declare format for logging to file
file_formatter = logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
)

# add file handler to application logger
from logging.handlers import RotatingFileHandler
log_path = app.instance_path[0:app.instance_path.index('instance')]
file_handler = RotatingFileHandler(log_path + 'debug.log')
file_handler.setLevel(LOG_LEVEL)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

import pmg_frontend.views
