import socket
import multiprocessing

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        number = int(data.decode())
        result = number ** 2
        conn.sendall(str(result).encode())
    conn.close()

def sequential_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 5000))
        s.listen()
        print("Server is running in sequential mode...")
        while True:
            conn, addr = s.accept()
            handle_client(conn, addr)

def parallel_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 5000))
        s.listen()
        print("Server is running in parallel mode...")
        while True:
            conn, addr = s.accept()
            process = multiprocessing.Process(target=handle_client, args=(conn, addr))
            process.start()

if __name__ == "__main__":
    mode = input("Enter server mode (sequential/parallel): ").strip().lower()
    if mode == "sequential":
        sequential_server()
    elif mode == "parallel":
        parallel_server()
    else:
        print("Invalid mode")
