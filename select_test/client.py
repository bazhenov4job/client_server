from socket import *
from select import select
import sys
import argparse

ADDRESS = ('localhost', 10000)
parser = argparse.ArgumentParser()
parser.add_argument('-m')
args = vars([parser.parse_args()])
try:
    MODE = args['-m']
except KeyError:
    MODE = 'r'


def echo_client():

    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(ADDRESS)
        while True:
            if MODE == 'w':
                msg = input('Ваше сообщение: ')
                if msg == 'exit':
                    break
                else:
                    sock.send(msg.encode('utf-8'))

            elif MODE == 'r':
                data = sock.recv(1024).decode('utf-8')
                print('Ответ: ', data)

        # sock.close()


echo_client()
