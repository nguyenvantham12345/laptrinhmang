import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12346))

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

client.send(f"{a} {b}".encode())
result = client.recv(1024).decode()

print(f"Các số chia hết cho 5 trong khoảng [{a}, {b}]: {result}")
client.close()
