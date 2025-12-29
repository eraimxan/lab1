import socket
import json
import time
import threading

HOST = "0.0.0.0"
PORT = 5000

# Request log for at-most-once (optional enhancement)
processed_requests = {}

def add(a, b):
    return a + b

def reverse_string(s):
    return s[::-1]

def handle_client(conn, addr):
    print(f"[+] Connection from {addr}")

    try:
        data = conn.recv(1024).decode()
        if not data:
            return

        request = json.loads(data)
        request_id = request["request_id"]
        method = request["method"]
        params = request["params"]

        print(f"[REQUEST] {request}")

        # 🔥 Artificial delay (for failure demo)
        if method == "add":
            time.sleep(5)  # simulate slow server

        if method == "add":
            result = add(params["a"], params["b"])
        elif method == "reverse_string":
            result = reverse_string(params["s"])
        else:
            raise Exception("Unknown method")

        response = {
            "request_id": request_id,
            "status": "OK",
            "result": result
        }

    except Exception as e:
        response = {
            "request_id": request_id if "request_id" in locals() else None,
            "status": "ERROR",
            "error": str(e)
        }

    conn.sendall(json.dumps(response).encode())
    conn.close()


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[SERVER] Listening on port {PORT}")

        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()


if __name__ == "__main__":
    start_server()
