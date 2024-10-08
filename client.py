import socket

# Tạo socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kết nối tới server
client_socket.connect(('localhost', 12345))

# Nhập vào 2 số từ người dùng
num1 = input("Nhập số thứ nhất: ")
num2 = input("Nhập số thứ hai: ")

# Gửi dữ liệu đến server
client_socket.send(f"{num1} {num2}".encode())

# Nhận kết quả từ server
result = client_socket.recv(1024).decode()

# In ra kết quả
print(f"Tổng của {num1} và {num2} là: {result}")

# Đóng kết nối
client_socket.close()
