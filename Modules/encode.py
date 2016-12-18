
import re
import sys

class Encode():

    def __init__(self, windows, buffer, char):
        self.sizeWin = windows
        self.sizeBuf = buffer
        self.sizeChar = char

    def _findMatch(self, win, buf):
        prev = ''
        while len(buf):
            ret = win.rfind(buf)
            if ret < 0:
                prev = buf[-1]
                buf = buf[:-1]
            else:
                self.pos = abs(ret - len(win))
                self.len = len(buf)
                if prev:
                    self.char = prev
                else:
                    self.char = chr(0)
                break
        return ret

    def _scrollDict(self, decal):
        self.win = self.win + self.buf[:decal]
        self.buf = self.buf[decal:]
        self.win = self.win[-self.sizeWin:]

    def _setEncode(self):
        match = self._findMatch(self.win, self.buf)
        if match >= 0:
            self.lst.append((self.pos, self.len, ord(self.char)))
            decal = self.len + 1
        else:
            self.lst.append((0, 0, ord(self.buf[0])))
            decal = 1
        return decal

    def encodeLZ77(self, txt):
        try:
            self.buf = ''
            self.win = ''
            self.lst = list()

            for c in txt:
                c = chr(c)
                if len(self.buf) < self.sizeBuf:
                    self.buf = self.buf + c
                if len(self.buf) >= self.sizeBuf:
                    decal = self._setEncode()
                    self._scrollDict(decal)

            while len(self.buf):
                decal = self._setEncode()
                self._scrollDict(decal)
        except:
            print ("Unexpected error:", sys.exc_info()[1])
            return self.lst

        return self.lst
