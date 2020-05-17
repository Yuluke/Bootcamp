from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    def __init__(self):
        Tk.__init__ (self)
        self.geometry ("272x300")
        self.title ("Calculadora")

    def start(self):
        self.mainloop()

if __name__=='__main__':
    app=mainApp()
    app.start()