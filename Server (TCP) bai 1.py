import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)
print("Server đang chờ kết nối...")

conn, addr = server.accept()
print(f"Kết nối từ {addr}")

data = conn.recv(1024).decode()
a, b = map(int, data.split())

result = " ".join(str(i) for i in range(a, b + 1))
conn.send(result.encode())

conn.close()
server.close()
