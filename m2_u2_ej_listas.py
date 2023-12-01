from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
import re
# ##############################################
# MODELO
# ##############################################
el_id = 0
la_lista = {}
total = 0

def alta(producto, cantidad, precio, tree):
    global el_id
    global la_lista

    cadena = producto
    patron="^[A-Za-záéíóú]*$"  #regex para el campo cadena
    if(re.match(patron, cadena)):
        fila = {str(el_id): [producto, cantidad, precio]}
        la_lista.update(fila)
        el_id +=1
        t_val.set("Consultar")
        print("Estoy en alta todo ok")
        actualizar_treeview(tree)
    else:
        print("error en campo producto")

def consultar():
    global total
    total = 0
    for i in la_lista:
        total += la_lista[i][1] * la_lista[i][2]

    t_val.set(total)

def borrar(tree):

    valor = tree.selection()
    # print(valor)   #('I005',)
    item = tree.item(valor)
    la_lista.pop(item["text"])
    t_val.set("Consultar")
    print("La seleccion fue eliminada")
    tree.delete(valor)

def actualizar_treeview(mitreview):
    global la_lista

    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    for fila in la_lista:
        mitreview.insert("", 0, text=fila, values=(la_lista[fila][0], la_lista[fila][1], la_lista[fila][2]))

# ##############################################
# VISTA
# ##############################################

root = Tk()
root.title("Tarea POO")
        
titulo = Label(root, text="Ingrese sus datos", bg="DarkOrchid3", fg="thistle1", height=1, width=60)
titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)

producto = Label(root, text="Producto")
producto.grid(row=1, column=0, sticky=W)
cantidad=Label(root, text="Cantidad")
cantidad.grid(row=2, column=0, sticky=W)
precio=Label(root, text="Precio")
precio.grid(row=3, column=0, sticky=W)
l_total = Label(root, text = "El total de la compra es:")
l_total.grid(row= 11, column= 0, sticky=E, columnspan= 2)

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
e_total.grid(row= 11, column= 2)

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
tree.grid(row=10, column=0, columnspan=4)

boton_alta=Button(root, text="Alta", command=lambda:alta(a_val.get(), b_val.get(), c_val.get(), tree))
boton_alta.grid(row=6, column=1)

boton_consulta=Button(root, text="Consultar", command=lambda:consultar())
boton_consulta.grid(row=7, column=1)

boton_borrar=Button(root, text="Borrar", command=lambda:borrar(tree))
boton_borrar.grid(row=8, column=1)
root.mainloop()