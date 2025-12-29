# RPC Lab — Distributed Computing (AWS EC2)

This repository contains a simple **RPC (Remote Procedure Call) implementation** using Python TCP sockets and JSON serialization.  
The lab demonstrates RPC communication, retries, timeout handling, and failure simulation using AWS EC2 instances.

---

## ✅ Features

- TCP socket-based client-server communication
- JSON message format
- Request ID (UUID), method name, arguments, timestamp
- Timeout and retry logic on client
- Failure handling demonstration (firewall block)
- At-least-once semantics

---

## 🔹 Files

| File | Description |
|------|-------------|
| `server.py` | RPC server that exposes remote functions and handles requests |
| `client.py` | RPC client that sends requests, handles retries, and prints results |
| `requirements.txt` | Python dependencies (only standard libraries are used) |
| `README.md` | Instructions for running the lab |

---

## 💻 Requirements

- Python 3.x
- Two AWS EC2 instances (Ubuntu 22.04 recommended)
- Open port 5000 in server security group
- SSH access to both instances

---

## 🚀 How to Run

### 1️⃣ Server (on `rpc-server-node` EC2)
```bash
sudo ufw allow 5000  # make sure port 5000 is open
python3 server.py
