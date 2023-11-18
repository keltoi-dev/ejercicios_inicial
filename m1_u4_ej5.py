# Ejercicio 5 - Unidad 4
# German Fraga

"""
Cree un programa que utilizando una función, solicite la edad de la persona e imprima todos los años que la persona ha cumplido según el siguiente formato de ejemplo.
1, 2, 3, 4, 5 Y
5, 4, 3, 2, 1
"""

def recorrer(desde, hasta, orden):
    lista = []
    cadena = ""
    for i in range(desde, hasta, orden):
        lista.append(str(i))
    cadena = ", ".join(lista)
    return cadena

edad = int(input("Ingrese su edad: "))
print(recorrer(1, edad + 1, 1))
print("\n  Y\n")
print(recorrer(edad, 0, -1))
