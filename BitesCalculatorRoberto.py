from math import log
print("-------------------------------")
print("-----ROBERTO'S-CALCULATOR------")
print("-------------------------------")
network1 = input("INSERT NETWORK 1 : ")
network2 = input("INSERT NETWORK 2 : ")
network3 = input("INSERT NETWORK 3 : ")
network4 = input("INSERT NETWORK 4 : ")
host = input("INSERT HOST:   ")
print("-------------------------------")
print("NETWORK    : ",network1,".",network2,".",network3,".",network4)
print("HOST       : ",host)
hostI = int(host)

def log2(x, base):
	return int(log(x) / log(base))
def findNextPowerOf2(hostI):
	hostI = hostI - 1
	lg = log2(hostI, 2)
	return 1 << lg + 1

hostRounded = findNextPowerOf2(hostI)
hostBits = None

if hostRounded == 0:
    hostBits = 0
elif hostRounded == 2:
    hostBits = 1
elif hostRounded == 4:
    hostBits = 2
elif hostRounded == 8:
    hostBits = 3
elif hostRounded == 16:
    hostBits = 4
elif hostRounded == 32:
    hostBits = 5
elif hostRounded == 64:
    hostBits = 6
elif hostRounded == 128:
    hostBits = 7
print("-------------------------------")
print("DEBUG")
print("ROUNDED TO : ", hostRounded)
print("POWER OF 2 : ", hostBits)
hostBitsI= int(hostBits)
print("-------------------------------")
ipV4 = int(32)
ipV4Bits = ipV4 - hostBitsI
print("IPV4 BITS  : ",ipV4Bits)
print("-------------------------------")
zeroBits = 32 - ipV4Bits
print("ZEROS      : ",zeroBits)
ip8 = None
ip16 = None
ip24 = None
ip32 = None

if zeroBits == 0:
    ip8 = 255
    ip16 = 255
    ip24 = 255
    ip32 = 1+2+4+8+16+32+64+128
elif zeroBits == 1:
    ip8 = 255
    ip16 = 255
    ip24 = 255
    ip32 = 2+4+8+16+32+64+128
elif zeroBits == 2:
    ip8 = 255
    ip16 = 255
    ip24 = 255
    ip32 = 2+4+8+16+32+64+128
elif zeroBits == 3:
    ip8 = 255
    ip16 = 255
    ip24 = 255
    ip32 = 4+8+16+32+64+128
elif zeroBits == 3:
    ip8 = 255
    ip16 = 255
    ip24 = 255
    ip32 = 8+16+32+64+128
elif zeroBits == 4:
    ip8 = 255
    ip16 = 255
    ip24 = 255
    ip32 = 16+32+64+128
elif zeroBits == 5:
    ip8 = 255
    ip16 = 255
    ip24 = 255
    ip32 = 32+64+128
elif zeroBits == 6:
    ip8 = 255
    ip16 = 255
    ip24 = 255
    ip32 = 64+128
elif zeroBits == 7:
    ip8 = 255
    ip16 = 255
    ip24 = 255
    ip32 = 128

jump = 256 - ip32
print("-------------------------------")
print("JUMP       : ",jump)
print("IP ADDRESS : ",ip8,".",ip16,".",ip24,".",ip32)
