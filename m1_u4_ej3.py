# Ejercicio 3 - Unidad 4
# German Fraga

"""
Crear una función lambda que sea equivalente a la siguiente función:
def sumar(valor1, valor2): 
    res = valor1 + valor2 
    return res
"""

resultado = lambda valor1, valor2: valor1 + valor2
print(f"El resultado de la suma es:", resultado(5, 20))
