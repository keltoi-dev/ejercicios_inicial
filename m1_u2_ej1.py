# Ejercicio 1 - Unidad 2 - Alternativa con if
# German Fraga

# Para ejecutar desde terminal: python m1_u2_ej1.py 8 15 16

import sys


def validate(valor):
    if valor % 2 == 0:
        return f"El numero {valor} es multiplo de 2"
    else:
        return f"El numero {valor} no es multiplo de 2"


print(validate(int(sys.argv[1])))
print(validate(int(sys.argv[2])))
print(validate(int(sys.argv[3])))
