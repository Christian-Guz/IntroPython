import os

os.system("cls")
print("|--------------COMPARADOR DE EDADES-----------------|")

edad1 = int(input("\nIngrese la edad de la primera persona: "))
edad2 = int(input("Ingrese la edad de la segunda persona: "))

if edad1 > edad2:
    print("\nLa primera persona es mayor")
else:
    if edad1 < edad2:
        print("\nLa segunda persona es mayor")
    else:
        print("\nLas dos personas tienen la misma edad")



