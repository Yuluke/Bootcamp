from tkinter import *
from tkinter import ttk
import calculator

class mainApp(Tk):
    def __init__(self):
        Tk.__init__ (self)
        self.geometry ("272x300")
        self.title ("Calculadora")
        self.pack_propagate(False)

        c =calculator.Controlator (self)
        c.pack(side=TOP, fill=BOTH) 

    def start(self):
        self.mainloop()

if __name__=='__main__':
    app=mainApp()
    app.start()