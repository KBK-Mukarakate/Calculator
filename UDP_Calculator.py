
# Name: UDP_Calculator.py
# Desc: application that interface with the server to calculate an equation
# provided by the user
# Auth: Kundai Mukarakate
# Date: 27/03/24

import socket

server_name = 'localhost'
server_port = 11001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM )

user_equation = input('Input your equation. \n')
client_socket.sendto(user_equation.encode(), (server_name, server_port))

answer, server_address = client_socket.recvfrom(2048)
print(answer)
client_socket.close()