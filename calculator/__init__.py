import tkinter as tk
from calculator.controls import Display, KeyBoard
from class_romannumbers import RomanNumber, RomanNumberError

WIDTH = 272
HEIGHT = 300
#Las creamos como constantes porque las vamos a usar

operaciones = {
    '+': lambda a,b: a + b,
    '-': lambda a,b: a - b,
    'x': lambda a,b: a * b,
    '/': lambda a,b: a // b
} 

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry(f"{WIDTH}x{HEIGHT}")

        self.reset()

        self.display = Display(self)
        self.display.pack()

        self.display.typing("Hola")

        KeyBoard(self, self.click).pack()

    def reset(self):
        self.value = ''
        self.op1 = self.op2 = self.operation = None
        self.equal = False
    
    def click(self, tecla):
        try:
            if tecla == 'AC':
                self.reset()
            elif tecla in operaciones:
                if self.operation:
                #Es lo mismo que poner if self.operation is not None
                    if self.equal:
                        resultado = RomanNumber(self.value)
                    else:
                        self.op2 = RomanNumber(self.value)
                        resultado = operaciones[self.operation](self.op1, self.op2)
                    self.op1 = resultado
                    self.op2 = None
                    self.value = resultado.simbolo
                else:
                    self.op1 = RomanNumber(self.value)
                self.operation = tecla
            elif tecla == '=':
                if self.equal:
                    resultado = operaciones[self.operation](RomanNumber(self.value), self.op2)
                else:
                    self.op2 = RomanNumber(self.value)
                    resultado = operaciones[self.operation](self.op1, self.op2)
                self.value = resultado.simbolo
            else:
                if self.equal:
                    self.reset()
                if self.operation is not None and self.op2 is None:
                    self.value = ''
                    self.op2 = '' #Le damos un valor '' para que sea distinto de None
                self.value += tecla
            self.display.typing(self.value) 
            self.equal = tecla == '=' #Esto es una operacion logica, si la tecla es igual a = va a ser True
        except RomanNumberError:
            self.value = 'ERROR'
            self.display.typing(self.value) 
            self.reset()

