from logging import Formatter, handlers, getLogger, INFO, StreamHandler
import sys


class ServerLog:

    def logEvent(self, message):

        _format = Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s")
        _handler = handlers.TimedRotatingFileHandler("server_log.txt", when='h', interval=24, encoding='utf-8')
        _handler.setLevel(INFO)
        _handler.setFormatter(_format)
        app_logger = getLogger('app.' + __name__)
        app_logger.addHandler(_handler)
        app_logger.setLevel(INFO)
        app_logger.info(message)
