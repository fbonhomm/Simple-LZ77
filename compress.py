from Modules.encode import *
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
    sys.stderr = sys.stdout

file = File(sys.argv[1], 'rb', sys.argv[2], 'wb+')
bit = Bit()
encode = Encode(bit.bitToValue(setting.pos), bit.bitToValue(setting.len), bit.bitToValue(setting.char))

output = 0
file.fdin.seek(setting.off, 0)
size = os.path.getsize(sys.argv[1])

tab = list()
tab.append(setting.pos)
tab.append(setting.len)
tab.append(setting.char)

def writeInFile(txt):
    global output

    output += 1
    file.put(bit.packer(1, int(txt[:8], 2)))
    txt = txt[8:]
    return txt

def encodeFile(lst, tab):
    txt = ''

    for cell in lst:
        for i in range(0, 3):
            byte = bin(cell[i])[2:]
            while len(byte) < tab[i]:
                byte = '0' + byte
            txt = txt + byte

        while len(txt) > 8:
            txt = writeInFile(txt)

    while len(txt) % 8:
        txt = '0' + txt
    while txt:
        txt = writeInFile(txt)

if __name__ == '__main__':
    txt = file.getFile()
    lst = encode.encodeLZ77(txt)
    encodeFile(lst, tab)

    print(" ------------------------------------------------------------------ \n",
            "Windows = %d, Buffer = %d\n" % (encode.sizeWin, encode.sizeBuf),
            "Numbers of bytes for encode: position = %d, length = %d, character = %d\n" % (tab[0], tab[1], tab[2]),
            "Offset = %d\n" % (setting.off),
            "Compression ratio: %d%%\n" % ((output * 100) / size),
            "------------------------------------------------------------------ ")
