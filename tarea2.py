import os

os.system("cls")

print("1: +\n2: -\n3: *\n4: /\nElija una número distinto para salir")

opc = int(input("\nElija una opción: "))

if opc != 1 and opc != 2 and opc != 3 and opc != 4:
    print("\nSalir")
else:
    num1 = int(input("\nAnote el primer número: "))
    num2 = int(input("\nAnote el segundo número: "))
    if opc == 1:
        suma = num1+num2
        print("\nEl resultado de la suma es: ",suma)
    else:
        if opc == 2:
            resta = num1-num2
            print("\nEl resultado de la resta es: ",resta)
        else:
            if opc == 3:
                mult = num1 * num2
                print("\nEl resultado de la umltiplicación es: ",mult)
            else:
                if opc == 4:
                    div = num1 / num2
                    print("\nEl resultado de la división es: ",div)