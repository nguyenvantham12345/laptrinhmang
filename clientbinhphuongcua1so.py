import socket

def send_number(number):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("localhost", 5000))
        s.sendall(str(number).encode())
        data = s.recv(1024)
        print(f"The square of {number} is {data.decode()}")

if __name__ == "__main__":
    number = int(input("Enter a number to send to the server: "))
    send_number(number)
