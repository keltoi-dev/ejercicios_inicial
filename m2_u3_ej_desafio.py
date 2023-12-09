"""
1) Crear una app que realice un alta de registros de los siguientes campos:

producto

descripción

2) La app debe estar realizada con tkinter y sqlite3
3) El campo "producto" debe de contener solo caracteres alfanuméricos.
4) La información debe poder presentarse en pantalla mediante un treeview
"""

from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
import re
import sqlite3

# ----- MODELO -----
# CONEXION CON LA BASE
def open_base():
    conexion = sqlite3.connect("m2_u3_database.db")
    return conexion

def create_table(conexion):
    cursor = conexion.cursor()
    sql = "CREATE TABLE listado(id integer PRIMARY KEY AUTOINCREMENT, \
    producto VARCHAR(20) NOT NULL, descripcion VARCHAR(50))"
    cursor.execute(sql)
    conexion.commit()

def create_record(producto, descripcion, tree):
    if not producto or not descripcion:
        l_status.config(text= "Complete todos los campos.", fg= "red")
    else:
        texto = producto
        patron = "^[a-zA-Z0-9 _]*$"
        if (re.match(patron, texto)):
            conexion = open_base()
            cursor = conexion.cursor()
            info = (producto, descripcion)
            sql = "INSERT INTO listado(producto, descripcion) VALUES (?, ?)"
            cursor.execute(sql, info)
            conexion.commit()
            var_product.set("")
            var_description.set("")
            update_tree(tree)
            l_status.config(text= "Se ha registrado correctamente la informacion.", fg= "black")
        else:
            l_status.config(text= "", fg= "black")
            showerror("ATENCION!!", "La informacion cargada es incorrecta.")

def update_tree(tree):
    conexion = open_base()
    cursor = conexion.cursor()
    sql = "SELECT * FROM listado"
    cursor.execute(sql)
    info = cursor.fetchall()

    records = tree.get_children()
    for element in records:
        tree.delete(element)

    for row in info:
        tree.insert("", 0, text= row[0], values= (row[1], row[2]))

try:
    conexion = open_base()
    create_table(conexion)
except:
    print("La base ya ha sido creada")

# ---- VISTA Y CONTROL -----

window = Tk()
window.title("Ejercicio - Modulo 2 - Unidad 3")

# Definir variables
var_product = StringVar()
var_description = StringVar()

# ----- Etiquetas y botones -----
l_title = Label(window, text= "Ingreso de datos", bg= "green", fg="#ffffff")
l_title.grid(row= 0, column= 0, columnspan= 3, sticky= W+E)
Label(window, text= "Producto").grid(row= 1, column= 0, sticky= E)
Label(window, text= "Descripcion").grid(row= 2, column= 0, sticky= E)
l_status = Label(window, text= "")
l_status.grid(row= 3, column= 0, columnspan= 3)

e_producto = Entry(window, textvariable= var_product, width= 50)
e_producto.grid(row= 1, column= 1)
e_descripcion = Entry(window, textvariable= var_description, width= 50)
e_descripcion.grid(row= 2, column= 1)

btn_create = Button(window, text= "Alta", bg= "#ff4444", fg= "#ffffff", font="bold")
btn_create.grid(row= 2, column= 2, padx= 5, pady= 5)

# ----- TreeView -----

tree = ttk.Treeview(window)
tree["columns"] = ("col1", "col2")
tree.column("#0", width= 30, minwidth= 15, anchor= W)
tree.column("col1", width= 120, minwidth= 80)
tree.column("col2", width= 300, minwidth= 120)
tree.heading("#0", text= "ID")
tree.heading("col1", text= "Producto")
tree.heading("col2", text= "Descripcion")
tree.grid(row= 4, column= 0, columnspan= 3)

btn_create.config(command= lambda: create_record(var_product.get(), var_description.get(), tree))

update_tree(tree)

window.mainloop()