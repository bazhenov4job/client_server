import time
import json
import sys
import os
module_path = os.path.split(os.getcwd())[0]
sys.path.insert(0, module_path)
from log.client_log_config import ClientLog
from log.server_log_config import ServerLog

client_logger = ClientLog()
utils_server_logger = ServerLog(r"log\utils_server_log.txt", 'utils_server_log')


def create_presence(user, password):
    """Создаёт сообщение присутствия на стороне клиента"""
    massage = {
        "action": "presence",
        "time": time.time(),
        "user": {
                "user": user,
                "password": password
        }
    }
    json_massage = json.dumps(massage)
    client_logger.logEvent("Создано сообщение присутствия")
    return json_massage


def send_message(socket, message):
    """Посылает сообщение от клиента на сторону сервера"""
    bytes_sent = socket.send(message.encode('utf-8'))
    client_logger.logEvent("Отправлено сообщение на сервер")
    return bytes_sent


def get_response(socket, bytes_to_read):
    """Получает ответ от сервера"""
    response = socket.recv(bytes_to_read)
    client_logger.logEvent("Получен ответ от сервера")
    return response


def handle_response(response):
    """обрабатывает полученный от сервера ответ"""
    string_response = response.decode('utf-8')
    json_response = json.loads(string_response)
    client_logger.logEvent("Ответ сервера обработан")
    return json_response


def get_message(client, bytes_to_read):
    """Функция на стороне сервера обрабатывает сообщение,
    полученное от клиента"""
    bytes_message = client.recv(bytes_to_read)
    message = json.loads(bytes_message.decode('utf-8'))
    utils_server_logger.logEvent("Сервер получил сообщение от клиента")
    return message


def create_response(message):
    """
    Создаёт отет для сообщения от клиента на стороне сервера

    :param message:
    :return:
    TODO: добавить проверки на ЛЮБЫЕ СООБЩЕНИЯ, в том числе те, в которых нет 'action'
    """
    try:
        message['action']
    except KeyError:
        utils_server_logger.logEvent("Неверное сообщение, отсутствует ключ")
    if message['action'] == "presence":
        response = {
            "response": 200,
            "alert": None
        }
        utils_server_logger.logEvent("Получено сообщение присутствия")
        return response
    else:
        response = {
            "response": 400,
            "alert": "Unknown action"
        }
        utils_server_logger.logEvent("Получено неизвестное сообщение")
        return response


def send_response(client, response):
    json_response = json.dumps(response)
    bytes_send = client.send(json_response.encode('utf-8'))
    return bytes_send
