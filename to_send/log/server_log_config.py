from logging import Formatter, handlers, getLogger, INFO, StreamHandler
import sys


_format = Formatter("%(asctime)-20s - %(levelname)-20s - %(module)s - %(message)s")
stream_format = Formatter("%(asctime)s - %(module)s - %(module)s")

_handler = handlers.TimedRotatingFileHandler("server_log.txt", when='h', interval=24, encoding='utf-8')
stream_handler = StreamHandler(sys.stderr)

stream_handler.setLevel(INFO)
_handler.setLevel(INFO)

_handler.setFormatter(_format)
stream_handler.setFormatter(stream_format)

app_logger = getLogger('app.' + __name__)
app_logger.addHandler(_handler)
app_logger.addHandler(stream_handler)
app_logger.setLevel(INFO)

app_logger.info("Some text")

