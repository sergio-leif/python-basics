"""

Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is 
a divisor of 26 because 26 / 13 has no remainder.)

"""

def calculate_divisors(number):
    lista = []
    i = 1
    while i < number:
        if number % i == 0: 
            lista.append(i)
        i+=1
    print(lista)

number = int(input("Indicate the number to calculate the divisors: "))
calculate_divisors(number)