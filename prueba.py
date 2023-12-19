# lista = [["" for _ in range(10)] for _ in range(1)]
# print(lista)

from tkinter import *
from tkinter.messagebox import *

window = Tk()

info = """
        Aplicacion para el manejo de una base de datos con 
        altas, bajas, modificaciones y consultas (CRUD), 
        para una nomina de empleados con una gran variedad 
        de datos.
        
        AUTOR: German Fraga"""

menubar = Menu(window, relief="solid")
menubar.add_cascade(label="Acerca de ...", command= lambda:showinfo("Acerca de ....", info))
window.config(menu=menubar)
window.mainloop()