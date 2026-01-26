import os

os.system("cls")

print("|---------------------Conteo en Binario-------------------|")

#Solicitud y comprobación
v = False
while v != True:
    num = int(input("\nIngrese un número del 1 al 100: ")) #Solicitud
    if num < 1 or num > 100:
        os.system("cls")
        print("\nNúmero fuera del rango, intente de nuevo") #Buscar si el número cumple
    else:
        v = True

print("\nNúmero valido: ", num) #Impresión de número

#Número a binario
bin = "" #Esto se pone para darle un valor a "bin" que no sea un número
i = num #Este valor lo guardo porque es el primer valor por el que se va adividir

while i > 0: #"i" al principio vale el número, después de covierte en el entero de la división
    bin = str(i % 2) + bin #Se divide entre "i" ya que se siguen dividiendo al entero
    i = i // 2 #Aquí es donde se obtiene el entero

print("El valor en binario es: ",bin)





