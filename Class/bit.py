
from struct import *
import math

class Bit():

    def reverseBinary(self, binary):
        return binary[::-1]

    def initMode(self, nbr):
        if nbr == 2:
            types = "H"
        elif nbr == 4:
            types = "I"
        elif nbr == 8:
            types = "L"
        else:
            types = "B"
        return types

    def packer(self, nbr, str):
        return pack(self.initMode(nbr), str)

    def unpacker(self, nbr, str):
        return unpack(self.initMode(nbr), str)[0]

    def bitToValue(self, opt):
        n = 1
        for i in range(0, opt):
            n *= 2
        return n - 1

    def valueToBits(self, nbr):
        n = math.log(nbr, 2)
        return math.ceil(n)

    def bitToByte(self, nb):
        return math.ceil(nb / 8)
