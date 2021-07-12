paciente1 = {"nombre":"Juan", "edad":42, "peso": 82.5, "fuma": False, "clinica": "El paciente presenta sintomas de tener X enfermedad"}
paciente2 = {"nombre":"Maria", "edad":23, "peso": 62.5, "fuma": False, "clinica": "El paciente presenta sintomas de tener Y enfermedad"}
paciente3 = {"nombre":"John", "edad":19, "peso": 82.5, "fuma": False, "clinica": "El paciente presenta sintomas de tener Z enfermedad"}

pacientes = [paciente1, paciente2, paciente3]

for x in range(len(pacientes)):
    print("")
    print("-------- DICCIONARIO N", x+1, "--------\n")
    #print(pacientes[x])
    for clave, valor in pacientes[x].items():
        print("-> ", clave,"\t|\t", valor)
    print("\n------------------------------------\n\n")


# Se puede utilizar rjust(10) para poner tabulaciones simulando columnas. Por ejemplo: print("Informacion: ".rjust(10))

"""
# Imprimir solo un diccionario
for clave, valor in paciente1.items():
    print("Clave -> ", clave)
    print("     Valor -> ", valor)
    if (clave == "edad" and valor < 33):
        print("Encontramos un paciente menor de 33")
"""

"""

demo = ["uno", "dos", "tres"]

# len(value) nos devuelve el tamaño de un contenedor llamado value
for x in range(len(demo)):
    print(demo[x])

"""

"""
# Obtener datos del diccionario
print(paciente["nombre"])
print(paciente["fuma"])

print(paciente.get("edad"))

# Obtener y borrar dato de diccionario
valor = paciente.pop("edad")
print(valor)
print(paciente)

# Actualizar valor en diccionario
paciente.update({"edad": 18})
paciente["edad"] = 23
print(paciente)

# Preguntar si se encuentra informacion en diccionario
print("peso" in paciente)

"""