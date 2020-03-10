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
from time import sleep
import argparse
from common import utils
from common import variables


USER = 'guest'
PASSWORD = 'password'
BYTES_TO_READ = variables.BYTES_TO_READ

parser = argparse.ArgumentParser()
parser.add_argument('-a')
parser.add_argument('-p')
args = vars(parser.parse_args())
try:
    HOST = args['-a']
except KeyError:
    HOST = variables.HOST

try:
    PORT = args['-p']
except KeyError:
    PORT = variables.PORT


sock = socket(AF_INET, SOCK_STREAM)
sock.connect((HOST, PORT))
message = utils.create_presence(USER, PASSWORD)
utils.send_message(sock, message)
response = utils.get_response(sock, BYTES_TO_READ)
handled_response = utils.handle_response(response)
for key, value in handled_response.items():
    print(key, value)
sock.close()
