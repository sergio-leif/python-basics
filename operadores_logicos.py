nublado = True
aburrido = True
# Contradecir boolean
entretenido = not(aburrido)

# Operador & es para decir tambien "and"
if nublado == True and aburrido == True:
    print("Vamos al cine")
else:
    print("Entonces nada")

"""
and -> true and true -> true
and -> true and false -> false
and -> false and false -> false
"""

# Operador "or"
if not(nublado == True) or aburrido == True:
    print("Vamos a hacer algo")
else:
    print("Entonces nada")

"""
or -> true or true -> true
or -> true or false -> true
or -> false or false -> false
"""