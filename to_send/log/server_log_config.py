import logging
import logging.handlers
import sys
import os
sys.path.append('../')

SERVER_FORMATTER = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s")
PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'server.log')

LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, when='h', interval=24, encoding='utf-8')
LOG_FILE.setFormatter(SERVER_FORMATTER)

LOGGER = logging.getLogger('server')
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(logging.INFO)
