# Ejercicio 10 - Unidad 3
# German Fraga

"""
Escriba un programa que guarde en una variable una contraseña y consulte 
al usuario por la contraseña hasta que esta sea correcta. El programa 
debe informar al usuario si la contraseña fue correcta o no.  
"""

password = "python"

valor = input("Ingrese la contraseña: ")

while password != valor:
    print("La contraseña es incorrecta")
    valor = input("Ingrese nuevamente la contraseña: ")

print("La contraseña es correcta")
