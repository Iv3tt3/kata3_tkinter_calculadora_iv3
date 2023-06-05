import tkinter as tk 

def imprimir_saludo():
    label.config(text=f"Hola, {valor_nombre.get()}")

root = tk.Tk()
root.title("Mi primera pantalla tkinter")

root.geometry("800x600+100+200")

label = tk.Label(root, text="", bd=2, relief=tk.RAISED, width=50) 
label.pack()

valor_nombre = tk.StringVar() 

nombre = tk.Entry(root, textvariable = valor_nombre) 
nombre.pack()

boton = tk.Button(root, text="Pulsame", command=imprimir_saludo) 
boton.pack()

root.mainloop()
