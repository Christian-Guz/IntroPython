import os

os.system("cls")

print("|--------------Calculo de Sueldo-------------|")

sueldo = int(input("\nAnote el sueldo del empleado: $"))

if sueldo < 1000:
    impuesto = 0
else:
    if sueldo >= 1000 and sueldo <= 2000:
        impuesto = sueldo * .10
    else:
        if sueldo > 2000:
            impuesto = sueldo * .20
            
print("\nEl impuesto a pagar es: $",impuesto) #Impuesto

sueldoN = sueldo - impuesto #Cálculo de sueldo Neto

print ("\nEl sueldo neto del empleado es de: $",sueldoN)