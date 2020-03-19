import select
from socket import socket, AF_INET, SOCK_STREAM


def read_requests(r_clients, all_clients):

    responses = {}
    for sock in r_clients:
        try:
            data = sock.recv(1024).decode('utf-8')
            responses[sock] = data

        except:
            print(f"Клиент {sock.fileno(), sock.getpeername()} откючился от нас")
            all_clients.remove(sock)

    return responses


def write_response(requests, w_clients, all_clients):

    for r_sock in requests:
        message = requests[r_sock]

        for w_sock in w_clients:
            if r_sock != w_sock:
                print(w_sock)
                try:
                    w_sock.send(message.encode('utf-8'))
                except:
                    print(f"Клиент {w_sock.fileno()} {w_sock.getpeername()} отключился.")
                    w_sock.close()
                    all_clients.remove(w_sock)


def main():

    address = ('', 10000)
    clients = []

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(5)
    sock.settimeout(0.2)
    while True:
        try:
            conn, addr = sock.accept()
            print(addr)
        except OSError as e:
            pass
        else:
            print(f"Получен запрос на взаимодействие от {addr}")
            clients.append(conn)
        finally:
            wait = 10
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass

            requests = read_requests(r, clients)

            if requests:
                write_response(requests, w, clients)


if __name__ == "__main__":
    main()
