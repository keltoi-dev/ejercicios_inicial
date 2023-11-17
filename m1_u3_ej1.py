# Ejercicio 1 - Unidad 3 - Alternativa con if y for/in
# German Fraga
"""
Tome el ejercicio de cálculo de números pares e impares de la unidad 2 y 
agréguele un bucle al código de forma de simplificarlo.
"""
# Para ejecutar desde terminal: python m1_u3_ej1.py 8 15 16

import sys


def validate(valor):
    if valor % 2 == 0:
        return f"El numero {valor} es multiplo de 2"
    else:
        return f"El numero {valor} no es multiplo de 2"


for i in range(1, 4):
    print(validate(int(sys.argv[i])))
