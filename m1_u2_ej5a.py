# Ejercicio 5 - Unidad 2
# German Fraga


def perimeter(radio):
    perimetro = 3.1416 * 2 * radio
    return perimetro


def superficie(radio):
    area = 3.1416 * (radio**2)
    return area


radio = int(input("Ingrese el valor del radio de la circunferencia: "))
resultado = perimeter(radio)
print("El perimetro de la circunferencia es:", resultado)
print("El area de la circunferencia es:", superficie(radio))
