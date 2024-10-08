import socket

# Tạo socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket tới địa chỉ IP và port
server_socket.bind(('localhost', 12345))

# Lắng nghe kết nối
server_socket.listen(1)
print("Server đang lắng nghe...")

# Chấp nhận kết nối từ client
conn, addr = server_socket.accept()
print(f"Kết nối từ: {addr}")

# Nhận dữ liệu từ client
data = conn.recv(1024).decode()
numbers = data.split()  # Chia dữ liệu nhận được thành các số

# Tính tổng 2 số
result = int(numbers[0]) + int(numbers[1])

# Gửi kết quả về client
conn.send(str(result).encode())

# Đóng kết nối
conn.close()
