import socket

print("Hostname:", socket.gethostname())
print("IP:", socket.gethostbyname(socket.gethostname()))

try:
    s = socket.create_connection(("lumeyana.local", 1883), timeout=5)
    print("Connection successful!")
    s.close()
except Exception as e:
    print("Connection failed:", e)