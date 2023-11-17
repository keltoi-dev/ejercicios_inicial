# Ejercicio 7 - Unidad 3
# German Fraga

"""
A partir del ejercicio 5 cree un programa que vaya 
agregando en un diccionario las compras realizadas.
"""

total = 0
posicion = {}
contador = 0

while True:
    cantidad = float(input("Ingrese la cantidad (0 = terminar): "))
    if cantidad == 0:
        break
    valor = float(input("Ingrese el precio: "))
    prov = {str(contador): [cantidad, valor, cantidad * valor]}
    posicion.update(prov)
    contador += 1

print("-" * 54)
print(f'{"Item":9} {"Cantidad":13} {"Precio":17} {"Total":12}')

for i in posicion:
    print(
        f"{i:4} {posicion[i][0]:12} {posicion[i][1]:12} {round((posicion[i][2]), 2):16}"
    )
    total += posicion[i][2]
print("-" * 54)
print(f"\nEl total de la compra es $ {total: .2f}")
