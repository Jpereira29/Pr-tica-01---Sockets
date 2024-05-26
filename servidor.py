import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('', 5000)
s.bind(server_address)
s.listen(1)
connection, address = s.accept()
data = connection.recv(1024)
if data:
  #connection.sendall(data)
  MSG = data.decode().upper()
  connection.sendall(str.encode(MSG))
connection.close()
s.close()