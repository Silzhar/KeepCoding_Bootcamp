import morse
from tkinter import *
from tkinter import ttk

class Translator(ttk.frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height=kwargs['height'], width=kwargs['width'])

        self.sender = StringVar()
        self.receiver = StringVar()

        sender_lbl = ttk.Label(self, text="Sender:", width=11, anchor=W)
        sender_lbl.place(x=12, y=12)
        self.sender_entry = ttk.Entry(self, width=16, textvariable=self.sender)
        self.sender_entry.place(x=70, y=10)
        
        receiver_lbl = ttk.Label(self, text="Receiver:", width=11, anchor=W)
        receiver_lbl.place(x=250, y=12)
        self.receiver_entry = ttk.Entry(self, width=16, textvariable=self.receiver)
        self.receiver_entry.place(x=318, y=10)
        
        origin_lbl = ttk.Label(self, text="Plano", width=5, anchor=W)
        origin_lbl.place(x=12, y=40)
        origin_text = Text(self, width=26,height=8)
        origin_text.place(x=32, y=60)

        destino_lbl = ttk.Label(self, text="Plano", width=5, anchor=W)
        destino_lbl.place(x=250, y=40)
        destino_text = Text(self, width=27,height=8)
        destino_text.place(x=270, y=60)

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
