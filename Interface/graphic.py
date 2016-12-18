from interface import *
from interComp import *
from interDecomp import *
from frame import *

inter = Interface("LZ77", 800, 600)
inter.resize(False, False)

inter.createTab("Compress")
inter.createTab("Decompress")

interComp(inter.tab[0], Frame(inter.tab[0], 600, 800))
interDecomp(inter.tab[1], Frame(inter.tab[1], 600, 800))

inter.window.mainloop()
