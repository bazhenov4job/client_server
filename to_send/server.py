from socket import *
import time
import argparse
from common import utils, variables
import sys
import os
sys.path.insert(0, os.getcwd())
from log.server_log_config import ServerLog

server_logger = ServerLog(r"log\server_log.txt", 'server_log')

BYTES_TO_READ = variables.BYTES_TO_READ

parser = argparse.ArgumentParser()
parser.add_argument('-a')
parser.add_argument('-p')
args = vars(parser.parse_args())
try:
    LISTEN = args['-a']
    server_logger.logEvent("Получен агрумент адреса хоста")
except KeyError:
    LISTEN = variables.HOST
    server_logger.logEvent("Адреса хоста выбран по умолчанию")

try:
    PORT = args['-p']
    server_logger.logEvent("Получен агрумент порта хоста")
except KeyError:
    PORT = variables.PORT
    server_logger.logEvent("Порт хоста выбран по умолчанию")

sock = socket(AF_INET, SOCK_STREAM)
sock.bind((LISTEN, PORT))
sock.listen(5)

client, addr = sock.accept()
message = utils.get_message(client, BYTES_TO_READ)
server_logger.logEvent(f"Сервер получил сообщение  \"{message}\" ")
response = utils.create_response(message)
utils.send_response(client, response)
client.close()
