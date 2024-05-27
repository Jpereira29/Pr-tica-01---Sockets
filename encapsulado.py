import socket
import multiprocessing


def servidor():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_address = ('', 5000)
  s.bind(server_address)
  s.listen(1)
  connection, address = s.accept()
  data = connection.recv(1024)
  if data:
    MSG = data.decode().upper()
    connection.sendall(str.encode(MSG))
  connection.close()
  s.close()

def cliente():
  server_address = ('127.0.0.1', 5000)

  MSG = 'Primeira mensagem em rede'

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(server_address)
  s.sendall(str.encode(MSG))
  data = s.recv(1024)

  print(data.decode())
  s.close()


if __name__ == '__main__':
  p1 = multiprocessing.Process(target=servidor)
  p2 = multiprocessing.Process(target=cliente)

  p1.start()
  p2.start()

  p1.join()
  p2.join()