import tkinter as tk

class Ventana(tk.Tk):
    #el padre es tk.Tk, por lo que heredamos todo lo que tiene Tk, los metodos, etc
    def __init__(self):
        #Tenemos que llamar al metodo init de su padre Tk
        super().__init__()
        #En este caso root es self
        self.title("Mi primera pantalla tkinter")
        self.geometry("800x600+400+200")
        self.label = tk.Label(self, text="", bd=2, relief=tk.RAISED, width=50) 
        self.label.pack()
        self.valor_nombre = tk.StringVar() 
        #Este input solo se usa una vez, cuando se crea y le damos valor, por lo que no necesito que sea un atributo. Label y valor_nombre en cambio, como lo necesitamos para el metodo, tienen que ser atributos
        nombre = tk.Entry(self, textvariable = self.valor_nombre) 
        nombre.pack()
        boton = tk.Button(self, text="Pulsame", command=self.imprimir_saludo) 
        boton.pack()
    
    def imprimir_saludo(self):
        self.label.config(text=f"Hola, {self.valor_nombre.get()}")

Ventana().mainloop()