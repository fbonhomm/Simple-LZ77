from tkinter import *
from tkinter.ttk import *

def interDecomp(win, frame):

    lstFile = list()
    lstFile.append(("Input File", lambda: frame.loadtemplate(win, 1)))
    lstFile.append(("Output File", lambda: frame.loadtemplate(win, 0)))

    n = 20
    for txt in lstFile:
        Button(win, text = txt[0], width = 15, command = txt[1]).place(x=frame.width / 2.75, y = n)
        n += 60

    lstLabel = list()
    lstLabel.append("- Numbers of bits encoding position and define size window\t\t\t      bits :")
    lstLabel.append("- Numbers of bits encoding length and define size buffer\t\t\t      bits :")
    lstLabel.append("- Numbers of bits encoding character\t\t\t\t\t      bits :")

    lstSpin = list()

    n = 150
    for txt in lstLabel:
        Label(win, text=txt).place(x=10, y = n + 2)
        spin = Spinbox(win, state="readonly", width=4, from_=0, to=64)
        spin.place(x=frame.width - 150, y = n)
        lstSpin.append(spin)
        n += 30

    Label(win, text="- Start Address (optional)").place(x=10, y=frame.height - 320)
    frame.createTxtDropDown(win, ('Decimal', 'Hexadecimal'))
    enter = Entry(win, width=20)
    enter.place(x=frame.width - 400, y=frame.height - 320)
    Button(win, text="Clean Console", width=15, command=lambda: frame.txt.delete(1.0, END)).place(x=frame.width - 250, y=frame.height - 270)
    Label(win, text="STDOUT:", font="Verdana 12 bold").place(x=15, y=frame.height - 260)
    frame.createTxtScroll(win, 8, 100)

    lstButton = list()
    lstButton.append(("Decompress", lambda: frame.execProg("./decompress.py", lstSpin, enter)))
    lstButton.append(("Information", lambda: frame.loadFile("./information.html")))
    lstButton.append(("Exit", frame.window.quit))

    n = frame.width / 8.5
    for txt in lstButton:
        Button(win, text=txt[0], width = 15, command = txt[1]).place(x = n, y=frame.height - 100)
        n += 200
