import socket, sys, re, pickle
from datetime import datetime

from colorama import Fore
lb = Fore.LIGHTBLUE_EX
b = Fore.BLUE
w = Fore.RESET

HOST = '127.0.0.1'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

  s.bind((HOST, PORT))
  s.listen()
  print(f'{b}Listening on {HOST}:{PORT}{w}')

  c, addr = s.accept()
  with c:
    while True:

      client_data = c.recv(4096).decode()
      server_time = datetime.now()

      # def send_data():
      #   c.send((server_data).encode())

      if not client_data:
        print(f'{lb}[{server_time}] {addr[0]} disconnected{w}')
        break
      
      # elif client_data == '/ping':
        # server_data = 
        # c.send(server_data.encode())

      elif client_data == '/client':
        pass

      elif client_data == '/server':
        server_data = [HOST, PORT] #, uptime, ping]
        c.send(pickle.dumps(server_data))

      else:
        print(f'{lb}[{server_time}] {addr[0]} ~ {w}{client_data}')

    c.close()