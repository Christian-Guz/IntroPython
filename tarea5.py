import os

os.system("cls")

"""Pedir al usuario 5 calificaciones, después de pedirlas, imprimiras el promdedio de esas 5 calficaciones"""

print("|--------------------Calculo de Promedio------------------|")

i = 1
suma = 0

while i <= 5:
    calf = int(input("\nAnote la califcación {}:".format(i)))
    i = i + 1
    suma = suma + calf
    
prom = suma / 5
print("\nEl promedio del alumno es: ",prom)