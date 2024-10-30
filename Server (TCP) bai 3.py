import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12347))
server.listen(1)
print("Server đang chờ kết nối...")

conn, addr = server.accept()
data = conn.recv(1024).decode()

numbers = list(map(float, data.split()))
numbers.sort()
result = " ".join(map(str, numbers))

conn.send(result.encode())
conn.close()
server.close()
