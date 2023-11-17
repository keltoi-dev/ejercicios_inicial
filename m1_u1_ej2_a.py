# Ejercicio 2 - Unidad 1 - Alternativa sin if
# German Fraga

# Para ejecutar desde terminal: python u1_ej2_a.py 8 15 16

import sys

valor_1 = int(sys.argv[1])
valor_2 = int(sys.argv[2])
valor_3 = int(sys.argv[3])

condicion_1 = valor_1 % 2 == 0
condicion_2 = valor_2 % 2 == 0
condicion_3 = valor_3 % 2 == 0

print(f"El {valor_1} es multiplo de 2?: {condicion_1}")
print(f"El {valor_2} es multiplo de 2?: {condicion_2}")
print(f"El {valor_3} es multiplo de 2?: {condicion_3}")
