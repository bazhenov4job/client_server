from socket import *
import time
import argparse
from common import utils, variables
from time import sleep


BYTES_TO_READ = variables.BYTES_TO_READ

parser = argparse.ArgumentParser()
parser.add_argument('-a')
parser.add_argument('-p')
args = vars(parser.parse_args())
try:
    LISTEN = args['-a']
except KeyError:
    LISTEN = variables.HOST

try:
    PORT = args['-p']
except KeyError:
    PORT = variables.PORT

sock = socket(AF_INET, SOCK_STREAM)
sock.bind((LISTEN, PORT))
sock.listen(5)

client, addr = sock.accept()
message = utils.get_message(client, BYTES_TO_READ)
print(message)
response = utils.create_response(message)
utils.send_response(client, response)
client.close()
sleep(1)
