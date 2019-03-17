import struct, socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn.connect(("127.0.0.1", 2998))

data = conn.recv(1024)

print(data)

wanted = str(struct.unpack("I", data)[0])

conn.sendall(wanted + '\n')

print(conn.recv(1024))
