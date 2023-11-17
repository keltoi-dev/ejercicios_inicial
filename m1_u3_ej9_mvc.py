# Ejercicio 9 - Unidad 3
# German Fraga

"""
A partir del ejerció 7 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada
"""


# Funcion de menu de opciones
def menu():
    opciones = "1234"
    print("\n")
    print("1 - Dar de alta a un item")
    print("2 - Dar de baja a un item")
    print("3 - Consultar los items cargados")
    print("4 - Modificar un item")
    print("\n0 - Salir y mostrar resumen\n")
    global seleccion
    global decision
    seleccion = input("selecciones una opcion: ")
    if seleccion in opciones:
        decision = True
    else:
        decision = False


# Funcion para dar de alta a un item
def alta(posicion: dict, contador: int):
    cantidad = float(input("Ingrese la cantidad: "))
    valor = float(input("Ingrese el precio: "))
    prov = {str(contador): [cantidad, valor, cantidad * valor]}
    posicion.update(prov)
    contador += 1

    return posicion, contador


# Funcion para dar de baja a un item determinado
def baja(posicion: dict):
    mostrar(posicion)

    x = input("\nIngrese que numero de item quiere dar de baja: ")
    if posicion.get(x, "no") == "no":
        print("El item no existe")
        return baja(posicion)
    posicion.pop(x)

    return posicion


# Funcion de consulta
def consulta(posicion: dict):
    total = mostrar(posicion)
    print(f"\nEl total de la compra es $ {total: .2f}")
    x = input("\nPresione una tecla para continuar")
    if x != "":
        return


# Funcion para modificar un item determinado
def modificar(posicion: dict):
    mostrar(posicion)

    x = input("\nIngrese que numero de item quiere modificar: ")
    if posicion.get(x, "no") == "no":
        print("El item no existe")
        return modificar(posicion)

    cantidad = float(input("Ingrese la cantidad a modificar: "))
    valor = float(input("Ingrese el precio a modificar: "))
    prov = {str(x): [cantidad, valor, cantidad * valor]}
    posicion.update(prov)

    return posicion


# Funcion para mostrar la compra
def mostrar(posicion: dict):
    total = 0
    print("-" * 47)
    print(f'{"Item":9} {"Cantidad":13} {"Precio":17} {"Total":12}')

    for i in posicion:
        print(
            f"{i:4} {posicion[i][0]:12} {posicion[i][1]:12} {round((posicion[i][2]), 2):16}"
        )
        total += posicion[i][2]
    print("-" * 47)

    return total


# Inicia mostrando un menu de opciones
posicion = {}
contador = 0

menu()
while decision:
    if seleccion == "1":
        posicion, contador = alta(posicion, contador)
        menu()
    elif seleccion == "2":
        posicion = baja(posicion)
        menu()
    elif seleccion == "3":
        consulta(posicion)
        menu()
    elif seleccion == "4":
        posicion = modificar(posicion)
        menu()

total = mostrar(posicion)
print(f"\nEl total de la compra es $ {total: .2f}")
