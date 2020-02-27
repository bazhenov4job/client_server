import time
import json


def create_presence(user, password):
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
    socket.send(message.encode('utf-8'))


def get_response(socket, bytes_to_read):
    response = socket.recv(bytes_to_read)
    return response


def handle_response(response):
    string_response = response.decode('utf-8')
    json_response = json.loads(string_response)
    return json_response


def get_massage(client, bytes_to_read):
    bytes_message = client.recv(bytes_to_read)
    message = json.loads(bytes_message.decode('utf-8'))
    return message


def create_response(message):
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
    client.send(json_response.encode('utf-8'))