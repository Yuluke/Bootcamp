from tkinter import *
from tkinter import ttk
class Controlator (ttk.Frame):
        def __init__(self,parent):
            ttk.Frame.__init__(self,parent,width=272,height=300)
            d= Display(self)
            d.grid (column=0, row=0, columnspan=4)

class Display (ttk.Frame):
        def __init__(self, parent):
            ttk.Frame.__init__(self, parent,width=272, height=50)
            self.pack_propagate(0)
            lbl=ttk.Label(self, text='0', anchor=E)
            lbl.pack(side=TOP, fill=BOTH, expand=TRUE)

class Selector ():
        pass
class CalcButton ():
        pass
