import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12349))

n = int(input("Nhập một số nguyên: "))
client.send(str(n).encode())

result = client.recv(1024).decode()
print(f"Tổng các chữ số của {n}: {result}")

client.close()
