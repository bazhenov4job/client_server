import time
import json


def create_presence(user, password):
    """Создаёь сообщение присутствия на стороне клиента"""
    massage = {
        "action": "presence",
        "time": time.time(),
        "user": {
                "user": user,
                "password": password
        }
    }
    json_massage = json.dumps(massage)

    return json_massage


def send_message(socket, message):
    """Посылает сообщение от клиента на сторону сервера"""
    bytes_sent = socket.send(message.encode('utf-8'))
    return bytes_sent


def get_response(socket, bytes_to_read):
    """Получает ответ от сервера"""
    response = socket.recv(bytes_to_read)
    return response


def handle_response(response):
    """обрабатывает полученный от сервера ответ"""
    string_response = response.decode('utf-8')
    json_response = json.loads(string_response)
    return json_response


def get_message(client, bytes_to_read):
    """Функция на стороне сервера обрабатывает сообщение,
    полученное от клиента"""
    bytes_message = client.recv(bytes_to_read)
    message = json.loads(bytes_message.decode('utf-8'))
    return message


def create_response(message):
    """
    Создаёт отет для сообщения от клиента на стороне сервера

    :param message:
    :return:
    TODO: добавить проверки на ЛЮБЫЕ СООБЩЕНИЯ, в том числе те, в которых нет 'action'
    """
    if message['action'] == "presence":
        response = {
            "response": 200,
            "alert": None
        }
        return response
    else:
        response = {
            "response": 400,
            "alert": "Unknown action"
        }
        return response


def send_response(client, response):
    json_response = json.dumps(response)
    bytes_send = client.send(json_response.encode('utf-8'))
    return bytes_send
