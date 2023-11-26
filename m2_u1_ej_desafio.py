# Ejercicio Desafio - Unidad 1
# German Fraga

from tkinter import *

# Funciones
def alta():
    print("Nueva alta de datos")
    titulo = w_titulo.get()
    ruta = w_ruta.get()
    descripcion = w_descripcion.get()
    print(titulo, ruta, descripcion)

def sorpresa():
    global color
    if color == 0:
        base.config(background = "#fddcb0")
        color = 1
    else:
        base.config(background = "#f0f0f0")
        color = 0

color = 0

# Interfaz grafica
base = Tk()
base.title("Ejercicio desafio")

# Definir variables Tk
w_titulo = StringVar()
w_ruta = StringVar()
w_descripcion = StringVar()

# Definir los widgets
titulo = Label(base, text = "Titulo")
titulo.grid(row = 0, column = 0, sticky = W)
ruta = Label(base, text = "Ruta")
ruta.grid(row = 1, column = 0, sticky = W)
descripcion = Label(base, text = "Descripcion")
descripcion.grid(row = 2, column = 0, sticky = W)

e_titulo = Entry(base, textvariable = w_titulo, width = 20)
e_titulo.grid(row = 0, column = 1)
e_ruta = Entry(base, textvariable = w_ruta, width = 20)
e_ruta.grid(row = 1, column = 1)
e_descripcion = Entry(base, textvariable = w_descripcion, width = 20)
e_descripcion.grid(row = 2, column = 1)

btn_alta = Button(base, text = "Alta", command = alta)
btn_alta.grid(row = 3, column = 1)
btn_sorpresa = Button(base, text = "Sorpresa", command = sorpresa)
btn_sorpresa.grid(row = 3, column = 2)

base.mainloop()

