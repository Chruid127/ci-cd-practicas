nombre = input("Ingrese su nombre: ")
print("Hola:" + nombre)
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("eres mayor de edad:", edad)
else:
    print("eres menor de edad:", edad)

if edad >= 18 and edad <= 25:
    print("Eres adulto joven")
elif edad > 25 and edad <= 60:
    print("Eres adulto")
elif edad > 60:
    print("Eres adulto mayor")
elif edad < 18 and edad >= 12:
    print("Eres un adolescente")
elif edad < 12 and edad >= 0:
    print("Eres un niño")