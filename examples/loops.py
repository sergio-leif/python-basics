
"""

total = 0
# Bucle for almacenando los valores en x
for x in range(7):
    print("Iteración número " + str(x))
    total += 5
    print("El total es -> " + str(total))

print("Finalizo el for")

"""

"""
# Este bucle for empieza desde el numero 2, en incrementos de 10 hasta 100

for x in range(2, 100, 10):
    print(x)

"""

participantes = 0
part_max = int(input("Por favor, ingresa la cantidad máxima de participantes: "))
print("")
# Otra forma de hacer print con string es como lo siguiente, con comas, el solito pone espacios:
print("El sistema ha sido configurado para aceptar a un máximo de",part_max," participantes. A partir de ahora, el sistema esta listo para admitir participantes")
print("")

# Tambien se puede poner -> while participantes in range(part_max):
while participantes < part_max:
    nombre = input("Ingrese su nombre: ")
    email = input("Ingrese su email: ")
    print("")
    print("Hola",nombre,"su email es",email,"desea confirmar inscripcion?")
    print("Para confirmar escriba \"SI\", para negar escriba \"NO\": ")
    # Siempre recoger el valor de entrada en minuscula
    respuesta = input().lower() # input().upper()
    print("")

    if respuesta == "si":
        print("**********************************")
        print("*Gracias, gracias por registrarse*")
        print("**********************************")
        participantes += 1
    else:
        print("*********************")
        print("*Operacion cancelada*")
        print("*********************")
    
    print("")
    print("Numero de participantes:",participantes)
    print("")

print("Capacidad maxima alcanzada")
