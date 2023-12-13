# Evaluacion final
# German Fraga

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

window = Tk()
window.title("Evaluacion final - Python inicial")
window.geometry("800x573")
window.resizable(False, False)

Label(window, text= "GESTION DE NOMINA DE EMPLEADOS", bg="#8BCC00", font= "Bold").grid(row= 0, column= 0, columnspan= 2, sticky= W+E)

# Definir variables
var_dni, var_cuil = IntVar(), IntVar()
var_nombre, var_apellido, var_domicilio = StringVar(), StringVar(), StringVar()
var_fnacimiento, var_falta, var_obra, var_art = StringVar(), StringVar(), StringVar(), StringVar()
var_jornal = float()
var_filtro = StringVar()

# Frame de menu
frame_menu = Frame(window, bg= "#c8c8c8", padx= 10, pady= 10, bd= 1, relief= "solid")
frame_menu.grid(row= 1, column= 0)

Label(frame_menu, text= "MENU", bg= "#c8c8c8", font= "Bold").grid(row= 0, column= 0, sticky= W+E)

btn_alta = Button(frame_menu, text= "ALTA", width= 15)
btn_alta.grid(row= 1, column= 0, padx= 9, pady= 8)
btn_baja = Button(frame_menu, text= "BAJA", width= 15)
btn_baja.grid(row= 2, column= 0, padx= 2, pady= 8)
btn_modificacion = Button(frame_menu, text= "MODIFICACION", width= 15)
btn_modificacion.grid(row= 3, column= 0, padx= 2, pady= 8)
btn_consulta = Button(frame_menu, text= "CONSULTA", width= 15)
btn_consulta.grid(row= 4, column= 0, padx= 2, pady= 8)
btn_cerrar = Button(frame_menu, text= "CERRAR", width= 15)
btn_cerrar.grid(row= 5, column= 0, padx= 2, pady= 8)

# Frame de datos
frame_datos = Frame(window, padx= 10, pady= 10, bd= 1, relief= "solid")
frame_datos.grid(row= 1, column= 1)

Label(frame_datos, text= "INFORMACION DEL EMPLEADO", font= "Bold").grid(row= 0, column= 0, columnspan= 6, pady= 10, sticky= W+E)

Label(frame_datos, text= "D.N.I.").grid(row= 1, column= 0, sticky= W)
Label(frame_datos, text= "C.U.I.L").grid(row= 1, column= 4, sticky= E)
Label(frame_datos, text= "NOMBRES").grid(row= 2, column= 0, sticky= W)
Label(frame_datos, text= "APELLIDOS").grid(row= 3, column= 0, sticky= W)
Label(frame_datos, text= "DOMICILIO").grid(row= 4, column= 0, sticky= W)
Label(frame_datos, text= "FECHA DE NAC.").grid(row= 5, column= 0, sticky= W)
Label(frame_datos, text= "FECHA DE ALTA").grid(row= 5, column= 4, sticky= E)
Label(frame_datos, text= "OBRA ASIGNADA").grid(row= 6, column= 0, sticky= W)
Label(frame_datos, text= "ART o SEGURO").grid(row= 7, column= 0, sticky= W)
Label(frame_datos, text= "JORNAL $").grid(row= 8, column= 0, sticky= W)

e_dni = Entry(frame_datos, textvariable= var_dni, width= 15)
e_dni.grid(row= 1, column= 1)
e_cuil = Entry(frame_datos, textvariable= var_cuil, width= 15)
e_cuil.grid(row= 1, column= 5)
e_nombre = Entry(frame_datos, textvariable= var_nombre, width= 80)
e_nombre.grid(row= 2, column= 1, columnspan= 5)
e_apellido = Entry(frame_datos, textvariable= var_apellido, width= 80)
e_apellido.grid(row= 3, column= 1, columnspan= 5)
e_direccion = Entry(frame_datos, textvariable= var_domicilio, width= 80)
e_direccion.grid(row= 4, column= 1, columnspan= 5)
e_fnacimiento = Entry(frame_datos, textvariable= var_fnacimiento, width= 15)
e_fnacimiento.grid(row= 5, column= 1)
e_f_alta = Entry(frame_datos, textvariable= var_falta, width= 15)
e_f_alta.grid(row= 5, column= 5)
e_obra = Entry(frame_datos, textvariable= var_obra, width= 80)
e_obra.grid(row= 6, column= 1, columnspan= 5)
e_art = Entry(frame_datos, textvariable= var_art, width= 80)
e_art.grid(row= 7, column= 1, columnspan= 5)
e_jornal = Entry(frame_datos, textvariable= var_jornal, width= 15)
e_jornal.grid(row= 8, column= 1)

btn_buscar = Button(frame_datos, text= "Buscar", width= 6)
btn_buscar.grid(row= 1, column= 2, sticky= W)

# Frame para treeview
frame_tree = Frame(window, padx= 10, pady= 10, bd= 0, relief= "solid")
frame_tree.grid(row= 2, column= 0, columnspan= 2)
frame_tree.config(width= 800, height= 180)

Label(frame_tree, text= "FILTRAR POR OBRA").grid(row= 0, column= 0, sticky= E)

e_filtro = Entry(frame_tree, textvariable= var_filtro, width= 80)
e_filtro.grid(row= 0, column= 1)

btn_filtrar = Button(frame_tree, text= "Filtrar")
btn_filtrar.grid(row= 0, column= 2, sticky= W)

tree = ttk.Treeview(frame_tree)
tree["columns"] = ("col1", "col2", "col3", "col4", "col5")
tree.column("#0", width= 20, minwidth= 10, anchor= W)
tree.column("col1", width= 80, minwidth= 50)
tree.column("col2", width= 200, minwidth= 80)
tree.column("col3", width= 200, minwidth= 80)
tree.column("col4", width= 180, minwidth= 80)
tree.column("col5", width= 100, minwidth= 80)
tree.heading("#0", text= "ID")
tree.heading("col1", text= "DNI")
tree.heading("col2", text= "NOMBRES")
tree.heading("col3", text= "APELLIDOS")
tree.heading("col4", text= "OBRA ASIGNADA")
tree.heading("col5", text= "JORNAL")
tree.grid(row= 1, column= 0, columnspan= 3)

# Label status
l_status = Label(window, text= "Ok.", bg= "#8BCC00")
l_status.grid(row= 3, column= 0, columnspan= 2, sticky= W+E)

window.mainloop()