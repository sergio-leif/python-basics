edad = int(input("Indica tu edad: "))
edad_limite = 17

# num1 = 10
# num2 = 20

# print(num1 > num2) # Esto es False

if edad > edad_limite:
    print("\n Bienvenido a nuestro sitio de inversiones online")

else:
    print("\n No tiene la edad necesaria para ingresar")

"""
70 helado
20 pastel
10 flan
"""

stock = input("Ingrese el postre encontrado: ")

if stock == "helado":
    print('Recuerda comprar las cucharas de plastico. No olvides el hielo!')
elif stock == "pastel":
    print("Recuerda comprar platos de plastico")
elif stock == "flan":
    print("Recuerda comprar platos de plastico")
else:
    print("Mejor no compres nada mas y llora")