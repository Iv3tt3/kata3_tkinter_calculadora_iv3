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

class CalcButton(tk.Frame):
    def __init__(self, location, command_function, text):
        super().__init__(location, width=68, height=50)
        self.pack_propagate(False)
        self.button = tk.Button(self, text=text, command=self.pressed)
        self.command_function = command_function 
        self.text = text
        #command espera que el parametro sea una receta (una funcion que pueda invocar), no el resultado de haber invocado la funncion
        self.button.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def pressed(self):
        self.command_function(self.text)



class KeyBoard(tk.Frame):
    def __init__(self, location, command_function):
        super().__init__(location, width=272, height=250)
        
        CalcButton(self, command_function,'AC').grid(row=0, column=0, columnspan=3, sticky='WE')
        CalcButton(self, command_function,'/').grid(row=0, column=3)
        CalcButton(self, command_function,'C').grid(row=1, column=0)
        CalcButton(self, command_function,'D').grid(row=1, column=1)
        CalcButton(self, command_function,'M').grid(row=1, column=2, rowspan=3, sticky='NS')
        CalcButton(self, command_function,'x').grid(row=1, column=3)
        CalcButton(self, command_function,'X').grid(row=2, column=0)
        CalcButton(self, command_function,'L').grid(row=2, column=1)
        CalcButton(self, command_function,'-').grid(row=2, column=3)
        CalcButton(self, command_function,'I').grid(row=3, column=0)
        CalcButton(self, command_function,'V').grid(row=3, column=1)
        CalcButton(self, command_function,'+').grid(row=3, column=3)
        CalcButton(self, command_function,'=').grid(row=4, column=0, columnspan=4, sticky='EW')