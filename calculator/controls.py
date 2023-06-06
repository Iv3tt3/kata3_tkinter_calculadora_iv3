import tkinter as tk
from tkinter.font import Font

class Display(tk.Frame):
    def __init__(self, location):
        super().__init__(location, width=272, height=50)
        self.pack_propagate(False) #Esto es para que el frame no se empaquete a la medida de la label
        f = Font(family='Helvetica',size=30, weight='bold')#Creamos una fuente
        self.label = tk.Label(self, background="#000000", foreground="#FFFFFF",
                              anchor=tk.E, padx=8, 
                              font=Font(family='Helvetica',size=27, weight='bold')) #Para anchor ver docs 5.5
        #La location de label va a ser el frame (self), no Calculator (location)
        #parametros: parent(location), color background, color texto, posicion texto
        self.label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    def typing(self,text):
        self.label.config(text=text) #**kwargs esto es un diccionario con la clave text, por eso no se lia python

