# Ejercicio 2 - Unidad 1 - Alternativa con if
# German Fraga

# Para ejecutar desde terminal: python u1_ej2_b.py 8 15 16

import sys

cantidad = len(sys.argv)
for i in range(1, cantidad):
    valor = int(sys.argv[i])
    if valor % 2 == 0:
        print(f"{valor} es multiplo de 2")
    else:
        print(f"{valor} no es multiplo de 2")
