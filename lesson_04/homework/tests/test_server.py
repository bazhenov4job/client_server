import unittest
import sys
sys.path.insert(0, r'D:\Programming\client_server\client_server\lesson_03\homework')
from common import utils
import json


class TestSocket:

    def send(self, message):
        return len(message)

    def recv(self, bytes_to_read):
        json_object = {'some': 'object'}
        str_object = json.dumps(json_object)
        try:
            str_object = str_object[:bytes_to_read]
        except IndexError:
            pass
        return str_object.encode('utf-8')


class TestGetMessage(unittest.TestCase):

    def testMessage(self):
        socket = TestSocket()
        test_response = {"some": "object"}
        bytes_to_read = len(json.dumps(test_response))
        response = utils.get_message(socket, bytes_to_read)
        self.assertEqual(test_response, response)


class TestCreateResponse(unittest.TestCase):

    def testResponsePresence(self):
        message = {"action": "presence"}
        response = utils.create_response(message)
        correct_responce = {
            "response": 200,
            "alert": None
        }
        self.assertEqual(correct_responce, response)

    def testWrongMessage(self):
        wrong_message = {"action": "abrakadabra"}
        correct_responce = {
            "response": 400,
            "alert": "Unknown action"
        }
        response = utils.create_response(wrong_message)

        self.assertEqual(correct_responce, response)


class TestSendResponse(unittest.TestCase):

    def testBytesSend(self):
        socket = TestSocket()
        json_message = {"some": "object"}
        correct_bytes = len(json.dumps(json_message).encode('utf-8'))
        bytes_send = utils.send_response(socket, json_message)
        self.assertEqual(correct_bytes, bytes_send)