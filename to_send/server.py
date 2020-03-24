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


def request(r_clients, all_clients):
    messages = {}
    for r_client in r_clients:
        try:
            message = utils.get_message(r_client, BYTES_TO_READ)
            messages[r_client] = message
        except OSError:
            server_logger.info(f"Похоже, клиент {r_client.fileno(), r_client.getpeername()} отключился")
            all_clients.remove(r_client)
    return messages


def response(r_clients, w_clients, all_clients, messages):
    for r_client, message in messages.items():
        for w_client in w_clients:
            if w_client != r_client:
                try:
                    utils.send_response(w_client, message)
                except:
                    server_logger.info(f"Похоже, клиент {w_client.fileno(), w_client.getpeername()}")
                    all_clients.remove(w_client)


def main_server():

    parser = argparse.ArgumentParser()
    parser.add_argument('-a')
    parser.add_argument('-p')
    args = vars(parser.parse_args())
    if args['a'] is not None:
        LISTEN = args['a']
        server_logger.info("Получен агрумент адреса хоста")
    else:
        LISTEN = variables.HOST
        server_logger.info("Адрес хоста выбран по умолчанию")

    if args['p'] is not None:
        PORT = args['p']
        server_logger.info("Получен агрумент порта хоста")
    else:
        PORT = variables.PORT
        server_logger.info("Порт хоста выбран по умолчанию")

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((LISTEN, PORT))
    sock.listen(5)
    sock.settimeout(1)
    clients = []
    while True:

        try:
            client, addr = sock.accept()
            clients.append(client)
        except OSError:
            print('Ошибка ОСИ')
        else:
            print(f"Получен запрос на взаимодействие от {addr}")

        finally:
            WAIT = 10
            r_clients = []
            w_clients = []
            try:
                # Вот тут хитрость.
                # r_clients - это объекты, которые готовы к получению данных (функция recv())
                # w_clients - это объекты, которые готовы к тому, чтобы данные отправить(send())
                r_clients, w_clients, e = select.select(clients, clients, [], WAIT)
                print(w_clients)
            except:
                pass

            #сперва проверим получили ли мы что-нибудь в сокеты
            messages = request(r_clients, clients)
            if messages:
                for r_client, message in messages.items():
                    server_logger.info(f"Сервер получил сообщение  \"{message}\" на сокет {r_client}")
                response(r_clients, w_clients, clients, messages)


if __name__ == '__main__':
    main_server()
