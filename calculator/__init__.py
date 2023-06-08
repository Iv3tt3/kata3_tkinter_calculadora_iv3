import tkinter as tk
from calculator.controls import Display, CalcButton

WIDTH = 272
HEIGHT = 300
#Las creamos como constantes porque las vamos a usar 

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry(f"{WIDTH}x{HEIGHT}")

        self.display = Display(self)
        self.display.pack()

        self.display.typing("Probando")

        button = CalcButton(self, self.click, '1') #En el command de calc buton le paso la funcion click
        button.pack()

        button2 = CalcButton(location=self, command_function=self.click2, text='2') 
        button2.pack()

        button3 = CalcButton(self, self.click, '3')
        button3.pack()

        button4 = CalcButton(self, self.click2, '4')
        button4.pack()

        self.display2 = Display(self)
        self.display2.pack()
        self.display2.typing("Probando")

    
    def click(self, tecla):
        self.display.typing(tecla) 

    
    def click2(self, tecla):
        self.display2.typing(tecla) 