# Ejercicio 2 - Unidad 3
# German Fraga

"""
Escriba un programa que consulte al usuario por una oración y 
comente al usuario cuantas veces aparece la letra “a”.
"""

oracion = input("Escriba una oracion: ")
contador = 0

for i in oracion:
    if i.lower() == "a":
        contador += 1

print("La letra a se repite {0} veces en la oracion".format(contador))
