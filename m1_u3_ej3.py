# Ejercicio 3 - Unidad 3
# German Fraga

"""
Escriba un programa que consulte al usuario por una oración y 
comente al usuario cuantas veces aparecen todas las vocales 
considerando minúsculas, mayúsculas y acentos.
"""

oracion = input("Ingrese una oracion: ")
contador = 0
letras = "aeiouáéíóúü"

for i in oracion:
    if i.lower() in letras:
        contador += 1

print("En la oracion hay {0} vocales".format(contador))
