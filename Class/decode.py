
import re
import sys

class Decode():

    def __init__(self, pb=2, lb=1, cb=1):
        self.posBytes = pb
        self.lenBytes = lb
        self.charBytes = cb

    def decodeLZ77(self, lst):
        txt = ''
        for cell in lst:
            if cell[0] == 0:
                txt += chr(cell[2])
            else:
                n = -cell[0] + cell[1]
                if n == 0:
                    tmp = txt[-cell[0]:]
                else:
                    tmp = txt[-cell[0]:n]
                txt = txt + tmp + chr(cell[2])
        return txt
