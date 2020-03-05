import logging


_format = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s")
_handler = logging.TimedRotatingFileHandler("client_log.txt")
