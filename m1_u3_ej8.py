# Ejercicio 8 - Unidad 3
# German Fraga

"""
A partir del ejerció 6 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada

"""


# Funcion para dar de alta a un item
def alta(posicion: list):
    cantidad = float(input("Ingrese la cantidad: "))
    valor = float(input("Ingrese el precio: "))
    total = cantidad * valor
    posicion.append([cantidad, valor, total])
    return posicion


# Funcion para dar de baja a un item determinado
def baja(posicion: list):
    mostrar(posicion)

    x = int(input("\nIngrese que numero de item quiere dar de baja: "))
    if x >= len(posicion):
        print("El item no existe")
        return baja(posicion)
    posicion.pop(x)
    return posicion


# Funcion de consulta
def consulta(posicion: list):
    x = ""
    total = mostrar(posicion)
    print(f"\nEl total de la compra es $ {total: .2f}")
    x = input("\nPresione una tecla para continuar")
    if x != "":
        return


# Funcion para modificar un item determinado
def modificar(posicion: list):
    mostrar(posicion)

    x = int(input("\nIngrese que numero de item quiere modificar: "))
    if x >= len(posicion):
        print("El item no existe")
        return modificar(posicion)

    cantidad = float(input("Ingrese la nueva cantidad: "))
    valor = float(input("Ingrese el nuevo precio: "))
    total = cantidad * valor
    posicion[x][0] = cantidad
    posicion[x][1] = valor
    posicion[x][2] = total

    return posicion


# Funcion para mostrar la compra
def mostrar(posicion: list):
    total = 0
    print("-" * 47)
    print(f'{"Item":9} {"Cantidad":13} {"Precio":17} {"Total":12}')

    for i in range(0, len(posicion)):
        print(
            f"{i:4} {posicion[i][0]:12} {posicion[i][1]:12} {round(posicion[i][2], 2):16}"
        )
        total += posicion[i][2]
    print("-" * 47)

    return total


# Inicia mostrando un menu de opciones
posicion = []

while True:
    opciones = "12340"
    print("\n\n")
    print("1 - Dar de alta a un item")
    print("2 - Dar de baja a un item")
    print("3 - Consultar los items cargados")
    print("4 - Modificar un item")
    print("\n0 - Salir y mostrar resumen\n")
    seleccion = input("selecciones una opcion: ")
    if seleccion in opciones:
        if seleccion == "1":
            posicion = alta(posicion)
        elif seleccion == "2":
            posicion = baja(posicion)
        elif seleccion == "3":
            consulta(posicion)
        elif seleccion == "4":
            posicion = modificar(posicion)
        else:
            break
    else:
        continue

total = mostrar(posicion)
print(f"\nEl total de la compra es $ {total: .2f}")
