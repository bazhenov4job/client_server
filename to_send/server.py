from socket import *
import logging
import argparse
from common import utils, variables
import sys
import os
import select
sys.path.insert(0, os.getcwd())
import log.server_log_config

server_logger = logging.getLogger('server')

BYTES_TO_READ = variables.BYTES_TO_READ


def request(w_clients, all_clients):
    messages = {}
    for w_client in w_clients:
        try:
            message = utils.get_message(w_client, BYTES_TO_READ)
            messages[w_client] = message
        except:
            print(f"Похоже, клиент {w_client.fileno(), w_client.getpeername()}")
            all_clients.remove(w_client)
    return messages


def response(w_clients, r_clients):
    pass


def main_server():

    parser = argparse.ArgumentParser()
    parser.add_argument('-a')
    parser.add_argument('-p')
    args = vars(parser.parse_args())
    try:
        LISTEN = args['a']
        server_logger.info("Получен агрумент адреса хоста")
    except KeyError:
        LISTEN = variables.HOST
        server_logger.info("Адреса хоста выбран по умолчанию")

    try:
        PORT = args['p']
        server_logger.info("Получен агрумент порта хоста")
    except KeyError:
        PORT = variables.PORT
        server_logger.info("Порт хоста выбран по умолчанию")

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((LISTEN, PORT))
    sock.listen(5)
    clients = []
    while True:

        try:
            client, addr = sock.accept()
        except OSError:
            print('Ошибка ОСИ')

        else:
            print(f"Получен запрос на взаимодействие от {addr}")

        finally:
            WAIT = 10
            client_to_read = []
            clients_to_write = []
            try:
                client_to_read, clients_to_write, e = select.select(clients, clients, [], WAIT)
            except:
                pass
            messages = request(clients_to_write, clients)
            server_logger.info(f"Сервер получил сообщение  \"{messages}\" ")

            # gone this far

            utils.send_response(client, response)
            client.close()


if __name__ == '__main__':
    main_server()
