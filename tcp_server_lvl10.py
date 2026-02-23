import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('', 6969))

print("[*] Bound to port 6969, but NOT listening yet.")
input("[*] Press ENTER to start listening (swap your symlink now)...")

server.listen(1)
conn, addr = server.accept()
print(f"[*] Connection accepted from {addr}")

data = conn.recv(4096)
print(f"[+] Received: {data.decode(errors='replace')}")

conn.close()
server.close()
