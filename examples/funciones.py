# Las funciones siempre se deben de crear antes de llamarlas
def calcula():
    calculo = 43 * 12 * 80
    calculo = calculo / 7
    print("El calculo es -> " + str(calculo))

# Funcion que recibe y devuelve parametros
def calcula_valor(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    return suma, resta

valor1, valor2 = calcula_valor(7, 8)
print("La suma es -> " + str(valor1))
print("La resta es -> " + str(valor2))