from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
import re
import sqlite3
# ##############################################
# MODELO
# ##############################################

# CONEXION CON LA BASE
def conectar_base():
    conexion = sqlite3.connect("m2_u2_database.db")
    return conexion

def hacer_tabla(conexion):
    cursor = conexion.cursor()
    sql = "CREATE TABLE compras(id integer PRIMARY KEY AUTOINCREMENT, \
    producto VARCHAR(20) NOT NULL, cantidad FLOAT, precio FLOAT)"
    cursor.execute(sql)
    conexion.commit()

def consulta_base():
    conexion = conectar_base()
    cursor = conexion.cursor()
    sql = "SELECT * FROM compras"
    cursor.execute(sql)
    la_lista = cursor.fetchall()
    return la_lista

total = 0
try:
    conexion = conectar_base()
    hacer_tabla(conexion)
except:
    print("La base ya ha sido creada")

# ----- FUNCION DE ALTA -----
def alta(producto, cantidad, precio, tree):

    cadena = producto
    patron="^[A-Za-záéíóú]*$"  #regex para el campo cadena
    if(re.match(patron, cadena)):
        conexion = conectar_base()
        cursor = conexion.cursor()
        datos = (producto, cantidad, precio)
        sql = "INSERT INTO compras(producto, cantidad, precio) VALUES (?, ?, ?)"
        cursor.execute(sql, datos)
        conexion.commit()

        calcular()
        print("Estoy en alta todo ok")
        actualizar_treeview(tree)
    else:
        print("error en campo producto")

# ----- FUNCION CALCULAR TOTAL -----
def calcular():
    total = 0
    la_lista = consulta_base()
    for i in la_lista:
        total += i[2] * i[3]

    t_val.set(total)

# ----- FUNCION DE CONSULTA -----
def consultar(tree):
    item = tree.item(tree.selection())
    conexion = conectar_base()
    cursor = conexion.cursor()
    el_id = int(item["text"])
    datos = (el_id, )
    sql = "SELECT * FROM compras WHERE id = ?;"
    cursor.execute(sql, datos)
    la_lista = cursor.fetchall()

    a_val.set(la_lista[0][1])
    b_val.set(la_lista[0][2])
    c_val.set(la_lista[0][3])

# ----- FUNCION DE MODIFICACION -----
def modificar(tree):
    item = tree.item(tree.selection())
    el_id = int(item["text"])
    producto = a_val.get()
    cantidad = b_val.get()
    precio = c_val.get()

    conexion = conectar_base()
    cursor = conexion.cursor()

    datos = (producto, cantidad, precio, el_id)
    sql = "UPDATE compras SET producto = ?, cantidad = ?, precio = ? WHERE id = ?;"
    cursor.execute(sql, datos)
    conexion.commit()
    print("La seleccion fue modificada")
    calcular()
    actualizar_treeview(tree)

# ----- FUNCION DE BORRAR -----
def borrar(tree):
    valor = tree.selection()
    item = tree.item(valor)
    conexion = conectar_base()
    cursor = conexion.cursor()
    el_id = int(item["text"])
    datos = (el_id, )
    sql = "DELETE FROM compras WHERE id = ?;"
    cursor.execute(sql, datos)
    conexion.commit()

    calcular()
    print("La seleccion fue eliminada")
    tree.delete(valor)

# ----- FUNCION ACTUALIZAR TREE -----
def actualizar_treeview(mitreview):
    la_lista = consulta_base()

    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    for fila in la_lista:
        mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))

# ##############################################
# VISTA
# ##############################################

root = Tk()
root.title("Tarea con Base de Datos")
        
titulo = Label(root, text="Ingrese sus datos", bg="DarkOrchid3", fg="thistle1", height=1, width=60)
titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)

producto = Label(root, text="Producto")
producto.grid(row=1, column=0, sticky=W)
cantidad=Label(root, text="Cantidad")
cantidad.grid(row=2, column=0, sticky=W)
precio=Label(root, text="Precio")
precio.grid(row=3, column=0, sticky=W)
l_total = Label(root, text = "El total de la compra es:")
l_total.grid(row= 12, column= 0, sticky=E, columnspan= 2)

# Defino variables para tomar valores de campos de entrada
a_val, b_val, c_val = StringVar(), DoubleVar(), DoubleVar()
t_val = StringVar()
w_ancho = 20

entrada1 = Entry(root, textvariable = a_val, width = w_ancho) 
entrada1.grid(row = 1, column = 1)
entrada2 = Entry(root, textvariable = b_val, width = w_ancho) 
entrada2.grid(row = 2, column = 1)
entrada3 = Entry(root, textvariable = c_val, width = w_ancho) 
entrada3.grid(row = 3, column = 1)
e_total = Entry(root, textvariable= t_val)
e_total.grid(row= 12, column= 2)

# --------------------------------------------------
# TREEVIEW
# --------------------------------------------------

tree = ttk.Treeview(root)
tree["columns"]=("col1", "col2", "col3")
tree.column("#0", width=90, minwidth=50, anchor=W)
tree.column("col1", width=200, minwidth=80)
tree.column("col2", width=200, minwidth=80)
tree.column("col3", width=200, minwidth=80)
tree.heading("#0", text="ID")
tree.heading("col1", text="Producto")
tree.heading("col2", text="cantidad")
tree.heading("col3", text="precio")
tree.grid(row=11, column=0, columnspan=4)

boton_alta=Button(root, text="Alta", command=lambda:alta(a_val.get(), b_val.get(), c_val.get(), tree))
boton_alta.grid(row=6, column=1)

boton_consulta=Button(root, text="Consultar", command=lambda:consultar(tree))
boton_consulta.grid(row=7, column=1)

boton_borrar=Button(root, text="Borrar", command=lambda:borrar(tree))
boton_borrar.grid(row=8, column=1)

boton_modificar=Button(root, text="Modifcar", command=lambda:modificar(tree))
boton_modificar.grid(row=9, column=1)

calcular()
actualizar_treeview(tree)

root.mainloop()