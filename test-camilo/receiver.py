import socket
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
port = int(os.getenv('PORT'))

def receive_message(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
        s.listen(1)
        print(f"Receiver listening on port {port}...")
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024).decode()
            print(f"Receiver received: {data}")

def receive_file(filename, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
        s.listen(1)
        print(f"Receiver listening on port {port}...")
        conn, addr = s.accept()
        with conn:
            with open(filename, 'wb') as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
            print(f"Receiver received: {filename}")

if __name__ == "__main__":
    #receive_message(port)
    filename = "received.txt"
    receive_file(filename, port)