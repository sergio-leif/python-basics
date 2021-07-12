
sabores = ["chocolate", "crema americana", "vainilla", True, 10, 12.3]
sabores2 = ["pistacho", "nata", "dulce de leche"]


"""

# Eliminar el PRIMER elemento que encuentre con el valor indicado
sabores.remove("crema americana")

"""

"""

# Añadir a una lista (sabores) la lista de sabores2 en el final
sabores.extend(sabores2)

"""

"""

# Insertar elemento en una posicion especifica
sabores.insert(0,"objeto insertado")

"""

"""

# Añadir elemento al final de la lista
sabores.append("Esto es el ultimo elemento")

"""

"""

# Eliminar un elemento de una lista, previamente obteniendolo
elemento_eliminado = sabores.pop(1)
print (elemento_eliminado)

"""

print(sabores)