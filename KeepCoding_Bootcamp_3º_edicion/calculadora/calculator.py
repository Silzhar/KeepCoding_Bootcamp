from tkinter import *
from tkinter import ttk

_heightBtn = 50
_widthBtn = 68

class CalcDisplay(ttk.frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height=_heightBtn, width=_widthBtn*4)

class Calculator(ttk.Frame):
    def __init(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height=kwargs['height'], width=kwargs['width'])



class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calculadora")
        self.geometry("272x300")

        self.calculator = Calculator(self, height=300, width=272)
        self.calculator.place(x=0, y=0)

    def start(self):
        self.mainloop()


if __name__== '__main__':
    app = MainApp()
    app.start()
