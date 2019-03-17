import struct, socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn.connect(("127.0.0.1", 2999))

data = conn.recv(1024)

print(data)

wanted = int(data.split("'")[1])

conn.sendall(struct.pack("I", wanted))

print(conn.recv(1024))
