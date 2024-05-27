import socket
server_address = ('192.168.56.1', 5000)

MSG = input("Digite um número: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server_address)
s.sendall(str.encode(MSG))
data = s.recv(1024)

print("O número ", MSG, "x 2 é: ", data.decode())
s.close()