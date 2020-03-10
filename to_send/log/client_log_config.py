from logging import Formatter, getLogger, INFO, FileHandler


class ClientLog:

    def _init__(self, file_address, logger_name):

        self.logger_name = logger_name
        self.file_address = file_address
        self._format = Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s")
        self._handler = FileHandler("client_log.txt", encoding='utf-8')
        self._handler.setLevel(INFO)
        self._handler.setFormatter(self._format)
        self.app_logger = getLogger(logger_name)
        self.app_logger.addHandler(self._handler)
        self.app_logger.setLevel(INFO)

    def logEvent(self, message):

        self.app_logger.info(message)
