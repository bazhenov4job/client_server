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


class TestCreatePresence(unittest.TestCase):

    def testMessageType(self):
        str_type = type('')
        message = utils.create_presence('spam', 'eggs')
        self.assertEqual(str_type, type(message))

    def testAction(self):
        action = 'presence'
        message = utils.create_presence('spam', 'eggs')
        dict_massage = json.loads(message)
        self.assertEqual(action, dict_massage['action'])

    def testUserPassword(self):
        user = 'user'
        password = 'password'
        message = utils.create_presence(user, password)
        dict_massage = json.loads(message)
        self.assertEqual((user, password),
                         (dict_massage['user']['user'], dict_massage['user']['password']))


class TestSendMessage(unittest.TestCase):

    def testBytesSend(self):
        socket = TestSocket()
        message = 'texts'
        bytes_send = utils.send_message(socket, message)
        self.assertEqual(bytes_send, len(bytes(message, 'utf-8')))


class TestGetResponse(unittest.TestCase):

    def testGetResponse(self):
        socket = TestSocket()
        test_response = {"some": "object"}
        bytes_to_read = len(json.dumps(test_response))
        response = utils.get_response(socket, bytes_to_read)
        response = json.loads(response.decode('utf-8'))
        self.assertEqual(test_response, response)


class TestHandleResponse(unittest.TestCase):

    def testResponseType(self):
        response = {"some": "object"}
        response_encoded = json.dumps(response).encode('utf-8')
        message_type = type(utils.handle_response(response_encoded))
        self.assertEqual(type(response), message_type)



