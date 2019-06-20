import morse
from tkinter import *
from tkinter import ttk

class Translator(ttk.frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height=kwargs['height'], width=kwargs['width'])


class MainApp(tk): # tk para crear ventana (hereda de tk)
    def __init__(self):
        Tk.__init__(self) # llama al constructor 
        self.title("Traductor morse")
        self.geometry("600x200")

        self.translator = Translator(self,height=200, width=600) # Translator(self) ancla la instancia en mainApp
        self.translator.place(x=0, y=0)
        

    def start(self): # self es la instancia que creamos
        self.mainloop() #repintar 

if __name__ == "__main__":
    translator = MainApp()
    translator.start()
