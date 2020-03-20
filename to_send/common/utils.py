import time
import json
import sys
import os
import logging
module_path = os.path.split(os.getcwd())[0]
sys.path.insert(0, module_path)
import log.client_log_config
import log.server_log_config
from decors import log

server_logger = logging.getLogger('server')
client_logger = logging.getLogger('client')


@log
def create_presence(user, password):
    """Создаёт сообщение присутствия на стороне клиента"""
    message = {
        "action": "presence",
        "time": time.time(),
        "user": {
                "user": user,
                "password": password
        }
    }
    json_message = json.dumps(message)
    client_logger.info("Создано сообщение присутствия")
    return json_message


@log
def create_message(client, text):
    """
    Формирует сообщение с указанием отправителя и проставлением временной метки
    :param client:
    :param text:
    :return:
    """
    message = {
        'action': 'msg',
        'time': time.asctime(),
        'to': '',
        'from': client,
        'encoding': 'utf-8',
        'message': text
    }
    json_message = json.dumps(message).encode('utf-8')
    return json_message


@log
def send_message(socket, message):
    """Посылает сообщение от клиента на сторону сервера"""
    bytes_sent = socket.send(message.encode('utf-8'))
    client_logger.info("Отправлено сообщение на сервер")
    return bytes_sent


@log
def get_response(socket, bytes_to_read):
    """Получает ответ от сервера"""
    response = socket.recv(bytes_to_read)
    client_logger.info("Получен ответ от сервера")
    return response


@log
def handle_response(response):
    """обрабатывает полученный от сервера ответ"""
    string_response = response.decode('utf-8')
    json_response = json.loads(string_response)
    client_logger.info("Ответ сервера обработан")
    return json_response


@log
def get_message(client, bytes_to_read):
    """Функция на стороне сервера обрабатывает сообщение,
    полученное от клиента"""
    bytes_message = client.recv(bytes_to_read)
    message = json.loads(bytes_message.decode('utf-8'))
    server_logger.info("Сервер получил сообщение от клиента")
    return message


@log
def create_response(message):
    """
    Создаёт отет для сообщения от клиента на стороне сервера

    :param message:
    :return:
    TODO: добавить проверки на ЛЮБЫЕ СООБЩЕНИЯ, в том числе те, в которых нет 'action'
    """
    response = {}
    try:
        message['action']
    except KeyError:
        server_logger.info("Неверное сообщение, отсутствует ключ")
        response = {
            "response": 400,
            "alert": "Unknown action"
        }
        server_logger.info("Получено неизвестное сообщение")
    else:
        if message['action'] == "presence":
            response = {
                "response": 200,
                "alert": None
            }
            server_logger.info("Получено сообщение присутствия")

        elif message['action'] == 'msg':
            response = message

    return response


@log
def send_response(client, response):
    json_response = json.dumps(response)
    bytes_send = client.send(json_response.encode('utf-8'))
    return bytes_send
