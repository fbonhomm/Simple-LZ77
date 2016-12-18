
class File():

    def __init__(self, input, mdin, output, mdout):
        self.fdin = open(input, mdin)
        self.fdout = open(output, mdout)

    def put(self, char):
        self.fdout.write(char)

    def getByte(self, nbr):
        return self.fdin.read(nbr)

    def getFile(self):
        return self.fdin.read()
