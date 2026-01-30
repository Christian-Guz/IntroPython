import os

os.system("cls")

print("|--------------------Multiplicador AxB----------------------|")

a = int(input("\nIngrese el número a: "))
b = int(input("Ingrese el número b: "))

cont = 1
suma = 0

while cont <= b:
    suma = suma + a
    cont +=1
    
cont = 1
    
print("\n")
while cont <= b:
    if cont < b:
        val = "{} + ".format(a)
        val2 = val * (b-1)
        cont +=1
    if cont == b:
        valI = "{} = ".format(a)
        val2 = val2 + valI
        cont +=1
     
print(val2, suma)