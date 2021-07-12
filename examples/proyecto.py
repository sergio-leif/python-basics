# Libreria para poder utilizar comandos del sistema operativo
import os   

def create_patient(name, age, weight, info):
    print("\nPlease, provide the next information:\n")
    patient = {"Name": name, "Age": int(age), "Weight": float(weight), "Info": info}
    #patients.insert(len(patients),patient)
    patients.append(patient)

def search_patient(name):
    print("\nInformation about " + name + ": \n")
    for x in range(len(patients)):
        if patients[x].get("Name") == name:
            for k, v in patients[x].items():
                print("-> ", k,"\t|\t", v)

def list_patients():
    print("\nPatients in the list:\n")
    for x in range(len(patients)):
        print("")
        print("----------- PATIENT N", x+1, "-----------\n")
        for k, v in patients[x].items():
            print("-> ", k,"\t|\t", v)
        print("\n------------------------------------\n\n")


option = 0
patients = []

print("\n")
print("######################################")
print("####### Welcome to my project ########")
print("######################################")

while option != 4:

    print("\nAvailable options: \n")
    print("\t 1 - Create patient")
    print("\t 2 - Search patient by name")
    print("\t 3 - List all patients")
    print("\t 4 - Exit")
    print("")
    option = int(input("Please, select an option: "))
    os.system("clear") # Metodo importado de la libreria os
    print("\n")

    if (option == 1):
        name = input("Write the name of the patient: ")
        age = int(input("Write the age of the patient: "))
        weight = float(input("Write the weight of the patient: "))
        info = input("If you want to give more info, please write here:\n")

        create_patient(name, age, weight, info)
    elif (option == 2):
        name = input("Write the name of the patient you want to find: ")
        search_patient(name)
    elif (option == 3):
        list_patients()
    else:
        print("Please, select an available option\n")

print ("\n Exiting of the app. Thank you for using us.")