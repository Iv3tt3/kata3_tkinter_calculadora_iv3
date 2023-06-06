import tkinter as tk
from calculator.controls import Display

WIDTH = 272
HEIGHT = 300
#Las creamos como constantes porque las vamos a usar 

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry(f"{WIDTH}x{HEIGHT}")

        display = Display(self)
        display.pack()

        display.typing("Probando")
    