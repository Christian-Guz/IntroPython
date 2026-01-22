import os

os.system("cls")

print("|----------------------Conteo de números----------------------|")

num = int(input("Ingrese un número (0 para terminar): "))
suma = 0

while num != 0:
    suma = suma + num
    num = int(input("Ingrese un número: (0 para terminar): "))
    
print("\nLa suma de los números ingresados es: ",suma)
    