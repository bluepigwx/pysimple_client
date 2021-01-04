# this is server

import socket
import sys


MAX_LISTEN_QUEUE=5
SERVER_PORT=9999

host_name = socket.gethostname()
print('server host name', host_name)

server_socket = socket.socket()
server_socket.bind((host_name, SERVER_PORT))

server_socket.listen(MAX_LISTEN_QUEUE)

print("server begin run")
server_run = True
while server_run :
    # 这里修改为非阻塞 todo
    client_socket, addr = server_socket.accept()
    print("new client addr", str(addr))

    server_run = False

    client_socket.close()

server_socket.close()

print("server finish")
    