# Ejercicio 5 - Unidad 3
# German Fraga

"""
Suponga que tiene una verdulería y carga la cantidad y el precio 
de lo comprado por un cliente. Realice un programa que tome de a 
uno la cantidad y el precio comprado por el cliente y al finalizar 
la compra retorne el monto total gastado.
"""
total = 0

while True:
    cantidad = float(input("Ingrese la cantidad (0 = terminar): "))
    if cantidad == 0:
        break
    valor = float(input("Ingrese el precio: "))
    total += cantidad * valor

print(f"\nEl total de la compra es $ {total: .2f}")
