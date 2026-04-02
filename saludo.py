nombre = input("¿Como te llamas?")
edad = int(input("¿Cuantos años tienes?"))

año_actual = 2026
nacimiento = año_actual - edad

print("Hola,", nombre)
print("Tu año de nacimiento aproximado es", nacimiento)

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")