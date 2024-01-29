import tkinter as tk

class Persona:
    def __init__(self):
        self.posx = 512
        self.posy = 512
        self.radio = 30
    def dibuja(self):
        lienzo.create_oval(
            self.posx-self.radio/2,
            self.posy-self.radio/2,
            self.posx+self.radio/2,
            self.posy+self.radio/2,
            fill="red")
        
raiz = tk.Tk()

lienzo = tk.Canvas(width=1024,height=1024)
lienzo.pack()

persona = Persona()
persona.dibuja()

raiz.mainloop()
