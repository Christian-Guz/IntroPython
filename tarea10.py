import os

os.system("cls")

print("|-----------------------Pirámide------------------------|")

x = int(input("\nIngrese un número: "))
y = "*"

for i in range(x+1):
    print(y * i)
    