# Ejercicio Numero factorial - Unidad 4
# German Fraga

def factor(factores: list, factoreo: int):
    numero = factores[-1]
    if numero == 1:
        return factores, factoreo
    elif numero == 0:
        return [], 1
    else:
        numero -= 1
        factoreo *= numero
        factores.append(numero)
        return factor(factores, factoreo)


num = 3

factores, factoreo = factor([num], num)
print("El factoreo es:", factores)
print("El resultodo del factoreo es:", factoreo)