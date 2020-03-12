import logging
import log.client_log_config
import log.server_log_config
import traceback
import inspect
import sys


if sys.argv[0].find('client') == -1:
    # если не клиент то сервер!
    LOGGER = logging.getLogger('server')
else:
    # ну, раз не сервер, то клиент
    LOGGER = logging.getLogger('client')


def log(func_to_log):
    """Функция декоратор"""
    def log_saver(*args, **kwargs):
        ret = func_to_log(*args, **kwargs)
        LOGGER.info(f'Была вызвана функция {func_to_log.__name__} c параметрами {args}, {kwargs}. '
                    f'Вызов из модуля {func_to_log.__module__}. Вызов из'
                    f' функции {traceback.format_stack()[0].strip().split()[-1]}.'
                    f'Вызов из функции {inspect.stack()[1][3]}')
        return ret
    return log_saver
