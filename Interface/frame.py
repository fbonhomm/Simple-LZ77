from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *

from urllib.request import pathname2url
import webbrowser

import os
import sys
import subprocess

class Frame():

    def __init__(self, win, h, w):
        self.window = win
        self.height = h
        self.width = w
        self.txt = list()
        self.input = ''
        self.output = ''
        self.labelInput = ''
        self.labelOutput = ''

    def createTxtScroll(self, win, h, w):
        self.txt = ScrolledText(win, wrap="word", height=h, width=w)
        self.txt.config(highlightbackground="black")
        self.txt.place(x=15, y=self.height - 240)

    def createTxtDropDown(self, win, tabl):
        self.ddown = Combobox(win ,textvariable=StringVar(), values =tabl, state='readonly', width=10)
        self.ddown.place(x=self.width - 200, y=self.height - 320)

    def execProg(self, file, lst, enter):
        if self.input and self.output:
            subprocess.call([sys.executable, os.path.abspath(file), self.input, self.output, lst[0].get(), lst[1].get(), lst[2].get(), enter.get(), self.ddown.get()])
            file = open('./stdout', 'r')
            text = file.read()
            self.txt.insert(END, text)
            file.close()
        else:
            print("File not set")

    def loadFile(self, path):
        url = 'file:{}'.format(pathname2url(os.path.abspath(path)))
        webbrowser.open(url)

    def loadtemplate(self, win, nb):
        filename = filedialog.askopenfilename()
        if filename:
            try:
                if nb:
                    self.input = filename
                    label = Label(win, text=filename, font="Verdana 13 bold")
                    label.place(x=30, y=52)
                    if self.labelInput:
                        self.labelInput.destroy()
                    self.labelInput = label
                else:
                    self.output = filename
                    label = Label(win, text=filename, font="Verdana 13 bold")
                    label.place(x=30, y=112)
                    if self.labelOutput:
                        self.labelOutput.destroy()
                    self.labelOutput = label
            except:
                messagebox.showerror("Open Source File", "Failed to read file \n'%s'" % filename)
