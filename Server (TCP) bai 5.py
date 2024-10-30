import socket

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12349))
server.listen(1)
print("Server đang chờ kết nối...")

conn, addr = server.accept()
data = conn.recv(1024).decode()

n = int(data)
result = sum_of_digits(n)

conn.send(str(result).encode())
conn.close()
server.close()
