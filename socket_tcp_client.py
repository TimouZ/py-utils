#!/usr/bin/env python3
import sys
import socket


if __name__ == '__main__':
    try:
        connection_port = int(sys.argv[1])
    except IndexError:
        connection_port = 8888
    print('Starting tcp client...')
    # print(f'Connected to: {}')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('', connection_port))
    while True:
        send_data = input('Send data: ').encode()
        sock.send(send_data)
        result = sock.recv(64).decode()
        print(f'Response: {result}')
    sock.close()

