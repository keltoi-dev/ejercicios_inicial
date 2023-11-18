# Ejercicio 7 - Unidad 4
# German Fraga

"""
Cree una función que tome la siguiente lista y reordene de menor a mayor sus componentes:
[3, 44, 21, 78, 5, 56, 9]
"""
contador = 0
lista = ["elemento1n1", "elemento2n1", "elemento3n1", 
        ["elemento1n2", "elemento2n2", "elemento3n2", 
        ["elemento1n3", "elemento2n3", "elemento3n3"]]]

def recorre_lista(item, espacio):
    global contador
    contador += 1
    print(espacio + "\n NIVEL", contador)
    for x in item:
        if isinstance(x, list): 
            recorre_lista(x, espacio + "   ")
        else: 
            print(espacio, x)

recorre_lista(lista, "")
