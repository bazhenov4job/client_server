"""
Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
клиент отправляет запрос серверу;
сервер отвечает соответствующим кодом результата. Клиент и сервер должны быть реализованы в виде отдельных скриптов,
содержащих соответствующие функции. Функции клиента: сформировать presence-сообщение; отправить сообщение серверу;
получить ответ сервера; разобрать сообщение сервера;
параметры командной строки скрипта client.py <addr> [<port>]: addr — ip-адрес сервера; port — tcp-порт на сервере,
по умолчанию 7777. Функции сервера: принимает сообщение клиента; формирует ответ клиенту; отправляет ответ клиенту;
имеет параметры командной строки: -p <port> — TCP-порт для работы (по умолчанию использует 7777)
; -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
"""


from socket import *
import argparse
from common import utils
from common import variables
import sys
import os
sys.path.insert(0, os.getcwd())
import logging
import log.client_log_config


client_logger = logging.getLogger('client')


def main_client():

    USER = 'guest'
    PASSWORD = 'password'
    BYTES_TO_READ = variables.BYTES_TO_READ

    parser = argparse.ArgumentParser()
    parser.add_argument('-a')
    parser.add_argument('-p')
    parser.add_argument('-m')
    args = vars(parser.parse_args())
    if args['a'] is not None:
        HOST = args['a']
        client_logger.info("Получен агрумент адреса хоста")
    else:
        HOST = variables.HOST
        client_logger.info("Адреса хоста выбран по умолчанию")

    if args['p'] is not None:
        PORT = args['p']
        client_logger.info("Получен агрумент порта хоста")
    else:
        PORT = variables.PORT
        client_logger.info("Порт хоста выбран по умолчанию")

    if args['m'] is None or args['m'] == 'r':
        MODE = 'r'
    else:
        MODE = 'w'

    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((HOST, PORT))

    while True:

        # message = utils.create_presence(USER, PASSWORD)
        if MODE == 'w':
            text = input("Введите сообщение для отправки:\n")
            if text == 'quit':
                break
            message = utils.create_message('w_client', text)
            utils.send_message(sock, message)
        elif MODE == 'r':
            response = utils.get_response(sock, BYTES_TO_READ)
            handled_response = utils.handle_response(response)
            try:
                handled_response.items()
                for key, value in handled_response.items():
                    client_logger.info(f"Получено сообщение{key}, {value}")
                print(handled_response['message'])
            except AttributeError:
                client_logger.info("Невозможно разобрать сообщение")


if __name__ == '__main__':
    main_client()
