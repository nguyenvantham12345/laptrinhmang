import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12347))

data = input("Nhập các số thực, cách nhau bằng khoảng trắng: ")
client.send(data.encode())

result = client.recv(1024).decode()
print(f"Chuỗi sắp xếp tăng dần: {result}")

client.close()
