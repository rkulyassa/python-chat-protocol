import socket, sys, re, pickle
from datetime import datetime

from colorama import Fore
lb = Fore.LIGHTBLUE_EX
b = Fore.BLUE
w = Fore.RESET

HOST = '127.0.0.1'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

  s.connect((HOST, PORT))
  print(f'{lb}[SERVER] {b}Connected to {HOST}:{PORT}{w}')

  while True:

    client_time = datetime.now().strftime('%H:%M:%S')
    client_data = input(f'{lb}[{client_time}] ~ {w}')

    def send_data():
      s.send(client_data.encode())
    def recv_data():
      return s.recv(4096)

    if client_data == '/quit' or client_data == '/disconnect':
      print(f'{lb}[SERVER] Connection ended{w}')
      break

    # elif client_data == '/ping':
    #   send_data()
    #   print(f'{lb}[SERVER] Ping: {recv_data().decode()}{w}')

    elif client_data == '/client':
      send_data()
      print(f'''\
{lb}Hostname: {socket.gethostname()}{w}
{lb}Localhost: {s.getsockname()[0]}{w}
{lb}Private IP: {socket.gethostbyname(socket.gethostname())}{w}
{lb}Port: {s.getsockname()[1]}{w}''')

    elif client_data == '/server':
      send_data()
      server_data = pickle.loads(recv_data())
      print(f'''\
{lb}Server IP: {server_data[0]}{w}
{lb}Server Port: {server_data[1]}{w}''')
# {lb}Uptime: {server_data[2]}{w}
# {lb}Ping: {server_data[3]}{w}''')

    else:
      send_data()

  s.close()