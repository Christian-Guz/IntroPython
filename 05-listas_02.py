import os

os.system("cls")

print("|-------------------Análisis de Sueldos------------------------|")
"Pedir 5 sueldos, agregar a lista e imprimir"

sueldo = []
cont = 0
suma = 0
mayor = 0
menor = 0

while cont <= 4:
    temp = float(input("\nIngrese el sueldo: "+str({cont+1})))
    sueldo.append(temp)
    suma = sueldo[cont] + suma
    
    if cont == 0:
        mayor = temp
        menor = temp
    else:
        if temp > mayor:
            mayor = temp
        if temp < menor:
            menor = temp
    cont +=1
    
    
print("\nLos sueldos son: ",sueldo)

#Promedio
prom = suma / cont 
print("\nEl promedio de los sueldos es: ",prom)
print("\nEl sueldo mayor es: ",mayor)
print("\nEl sueldo menor es: ",menor)


    