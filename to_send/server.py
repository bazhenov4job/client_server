from socket import *
import logging
import argparse
from common import utils, variables
import sys
import os
sys.path.insert(0, os.getcwd())
import log.server_log_config

server_logger = logging.getLogger('server')

BYTES_TO_READ = variables.BYTES_TO_READ


def main_server():

    parser = argparse.ArgumentParser()
    parser.add_argument('-a')
    parser.add_argument('-p')
    args = vars(parser.parse_args())
    try:
        LISTEN = args['-a']
        server_logger.info("Получен агрумент адреса хоста")
    except KeyError:
        LISTEN = variables.HOST
        server_logger.info("Адреса хоста выбран по умолчанию")

    try:
        PORT = args['-p']
        server_logger.info("Получен агрумент порта хоста")
    except KeyError:
        PORT = variables.PORT
        server_logger.info("Порт хоста выбран по умолчанию")

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((LISTEN, PORT))
    sock.listen(5)
    while True:

        client, addr = sock.accept()
        message = utils.get_message(client, BYTES_TO_READ)
        server_logger.info(f"Сервер получил сообщение  \"{message}\" ")
        response = utils.create_response(message)
        utils.send_response(client, response)
        client.close()


if __name__ == '__main__':
    main_server()
