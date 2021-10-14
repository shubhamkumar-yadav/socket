import socket
SRV_ADDR = input("Type the server ip address :")
SRV_PORT = int(input("Type the server port :"))
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind((SRV_ADDR,SRV_PORT))
s.listen(1)
print("Server started : waiting for connections....")
connection,address = s.accept()
print("client connect with address :", address)
while:
    data = connection.recv(1024)
    if not data : break
    connection.sendall(b'---message received---\n')
    print(data.decode('utf-8'))
connection.close()    