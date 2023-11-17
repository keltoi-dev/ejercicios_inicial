# Ejercicio diccionarios - Unidad 1
# German Fraga

person_1 = {
    "nombre": "Juan",
    "apellido": "Gomez",
    "edad": 45,
    "email": "juangomez@familia.org",
}
print("Tipo dato 1: ", type(person_1))
person_2 = {
    "nombre": "Maria",
    "apellido": "Juarez",
    "edad": 40,
    "email": "mariajuarez@familia.org",
}
print("Tipo dato 2: ", type(person_2))
person_3 = {
    "nombre": "Ramiro",
    "apellido": "Gomez",
    "edad": 15,
    "email": "ramirogomez@familia.org",
}
print("Tipo dato 3: ", type(person_3))
person_4 = {
    "nombre": "Julieta",
    "apellido": "Gomez",
    "edad": 10,
    "email": "julietagomez@familia.org",
}
print("Tipo dato 4: ", type(person_4))
familia = {"padre": person_1, "madre": person_2, "hijo": person_3, "hija": person_4}
print("---" * 20)
print(familia)
print(type(familia))
