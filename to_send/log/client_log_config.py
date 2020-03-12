import logging
import sys
import os
sys.path.append('../')

CLIENT_FORMATTER = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s")
PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'client.log')

LOG_FILE = logging.FileHandler(PATH, encoding='utf-8')
LOG_FILE.setFormatter(CLIENT_FORMATTER)

LOGGER = logging.getLogger('client')
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(logging.INFO)
