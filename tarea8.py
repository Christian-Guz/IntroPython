import os

os.system("cls")

print("|---------------------Tablas de multiplicar------------------------|")

num = int(input("Ingrese un número: ")) #Solicitar número

print("\nNúmero: ",num) #Imprimir número ingresado

for x in range(1,11): #"x" toma el valor del 1 al 10
    print("{} * {} = {}".format(num,x,num*x))
    