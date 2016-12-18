from tkinter.ttk import *
from tkinter import *

class Interface():

    def __init__(self, title='notTitle', w=100, h=100):
        self.window = Tk()
        self.window.title(title)
        self.window.geometry("%dx%d+%d+%d" % (w, h, w, h))
        self.root = Notebook(self.window)
        self.tab = list()
        self.width = w
        self.height = h

    def resize(self, width=False, height=False):
        self.window.resizable(width, height)

    def createTab(self, title):
        win = Frame(self.root, width=self.width, height=self.height)
        self.root.add(win, text=title)
        self.tab.append(win)
        self.root.pack()
