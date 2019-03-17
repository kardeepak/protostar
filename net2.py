import struct, socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn.connect(("127.0.0.1", 2997))

data = ""

while len(data) != 16:
	data += conn.recv(1024)

unpacked = sum([struct.unpack("I", data[i:i+4])[0] for i in range(0, len(data), 4)])

wanted = struct.pack("I", unpacked)

conn.sendall(wanted + '\n')

print(conn.recv(1024))
