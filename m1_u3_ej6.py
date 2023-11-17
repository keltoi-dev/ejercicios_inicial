# Ejercicio 6 - Unidad 3
# German Fraga

"""
A partir del ejercicio 5 cree un programa que vaya 
agregando en una lista las compras realizadas.
"""

total = 0
posicion = []

while True:
    cantidad = float(input("Ingrese la cantidad (0 = terminar): "))
    if cantidad == 0:
        break
    valor = float(input("Ingrese el precio: "))
    total += cantidad * valor
    posicion.append([cantidad, valor])

print("-" * 54)
print(f'{"Item":9} {"Cantidad":13} {"Precio":17} {"Total":12}')

for i in range(0, len(posicion)):
    print(
        f"{i:4} {posicion[i][0]:12} {posicion[i][1]:12} {round((posicion[i][0] * posicion[i][1]), 2):16}"
    )
print("-" * 54)
print(f"\nEl total de la compra es $ {total: .2f}")
