from logging import Formatter, getLogger, INFO, FileHandler


_format = Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s")
_handler = FileHandler("client_log.txt", encoding='utf-8')
_handler.setLevel(INFO)
_handler.setFormatter(_format)
app_logger = getLogger('app.' + __name__)
app_logger.addHandler(_handler)
app_logger.setLevel(INFO)

