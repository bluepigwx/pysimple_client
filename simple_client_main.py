# this is client

import socket
import sys

SERVER_PORT=9999

client_socket = socket.socket()
host = socket.gethostname()

client_socket.connect((host, SERVER_PORT))

client_run = True
while client_run:
    data = input(">>").strip()
    if not data:
        client_run = False
        break
    
    client_socket.send(data.encode("utf-8"))

client_socket.close()

print("finish client")