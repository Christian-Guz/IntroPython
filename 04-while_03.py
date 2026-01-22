import os
op = 0

while op != 5:
    os.system("cls")
    print("1.- Suma\n2.- Resta\n3.- Multiplicación\n4.- División\n5.- Salir")
    op = int(input("Selecciona una opción (1-5): "))
    if op == 1:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print("La suma de {} + {} es: {}".format(num1, num2, num1 + num2))
        input("Presiona Enter para continuar...")
    if op == 2:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print("La resta de {} - {} es: {}".format(num1, num2, num1 - num2))
        input("Presiona Enter para continuar...")
    if op == 3:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print("La multiplicación de {} * {} es: {}".format(num1, num2, num1 * num2))
        input("Presiona Enter para continuar...")
    if op == 4:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        if num2 != 0:
            print("La división de {} / {} es: {}".format(num1, num2, num1 / num2))
        else:
            print("Error: No se puede dividir entre cero.")
        input("Presiona Enter para continuar...")
        