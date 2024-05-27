import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('', 5000)
s.bind(server_address)
s.listen(1)
connection, address = s.accept()
data = connection.recv(1024)
if data:
  MSG = float(data.decode())
  MSG = MSG * 2
  connection.sendall(str.encode(str(MSG)))
connection.close()
s.close()