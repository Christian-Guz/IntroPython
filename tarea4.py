import os

os.system("cls")

print("|--------------------Calificaiones----------------------")

calf = int(input("\nAnote su calificacion: "))

if calf >= 7:
    if calf >= 9:
        print("\nExcelente")
    else:
        print("\nAprobado")
else:
    print("\nReprobado")

