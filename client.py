import socket
import json
import uuid
import time

SERVER_IP = "<SERVER_PUBLIC_IP>"
PORT = 5000

TIMEOUT = 2
MAX_RETRIES = 3

def rpc_call(method, params):
    request_id = str(uuid.uuid4())
    request = {
        "request_id": request_id,
        "method": method,
        "params": params,
        "timestamp": time.time()
    }

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"[CLIENT] Attempt {attempt} for request {request_id}")

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(TIMEOUT)
                s.connect((SERVER_IP, PORT))
                s.sendall(json.dumps(request).encode())

                response = s.recv(1024).decode()
                response = json.loads(response)

                print("[CLIENT] Response received:", response)
                return response

        except socket.timeout:
            print("[CLIENT] Timeout occurred, retrying...")
        except Exception as e:
            print("[CLIENT] Error:", e)

    print("[CLIENT] RPC failed after retries")
    return None


if __name__ == "__main__":
    rpc_call("add", {"a": 5, "b": 7})
