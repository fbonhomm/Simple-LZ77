from Modules.decode import *
from Modules.file import *
from Modules.bit import *

import os
import sys
import setting

if len(sys.argv) == 8:
    setting.pos = int(sys.argv[3], 10)
    setting.len = int(sys.argv[4], 10)
    setting.char = int(sys.argv[5], 10)
    if sys.argv[6] and sys.argv[7]:
        if sys.argv[7] == 'Decimal':
            setting.off = int(sys.argv[6], 10)
        else:
            setting.off = int(sys.argv[6], 16)
    sys.stdout = open('./stdout', 'w+')

file = File(sys.argv[1], 'rb', sys.argv[2], 'wb+')
bit = Bit()
decode = Decode(bit.bitToValue(setting.pos), bit.bitToValue(setting.len), bit.bitToValue(setting.char))

file.fdin.seek(setting.off, 0)
size = os.path.getsize(sys.argv[1])
txt = ''

def _setList(bits):
    global size
    global txt
    i = 0
    if len(txt) < bits:
        while i < bit.bitToByte(bits):
            byte = bin(bit.unpacker(1, file.getByte(1)))[2:]
            while len(byte) < 8:
                byte = '0' + byte
            txt += byte
            i += 1
        size -= bit.bitToByte(bits)
    ch = int(txt[:bits], 2)
    txt = txt[bits:]
    return ch


def decodeFile():
    lst = list()
    while size > 0:
        try:
            p = _setList(setting.pos)
            l = _setList(setting.len)
            c = _setList(setting.char)

            lst.append((p, l, c))
        except:
            print ("Unexpected error:", sys.exc_info()[1])
            return lst
    return lst


if __name__ == '__main__':
    lst = decodeFile()
    txt = decode.decodeLZ77(lst)
    for c in txt:
        file.put(bit.packer(1, ord(c)))

    print(" ------------------------------------------------------------------ \n",
            "Numbers of bytes for decode: position = %d, length = %d, character = %d\n" % (setting.pos, setting.len, setting.char),
            "Offset = %d\n" % (setting.off),
            "------------------------------------------------------------------ ")
