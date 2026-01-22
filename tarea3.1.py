import os

os.system("cls")

print("|---------------Calculadora de áreas----------------|")

print("1.Triángulo\n2.Cuadrado\n3.Círculo\n4.Pentágono\n5.Salir")
opc = int(input("\nElija una opción:"))

if opc == 5:
    print("\nSaliendo...")
else:
    if opc == 1:
        fig = "triángulo"
        print("\nFigura seleccionada: Triágulo")
        b = int(input("Anote la medida de la base: "))
        h = int(input("Anote la medida de la altura: "))
        area = (b * h) / 2
    else:
        if opc == 2:
            fig = "cuadrado"
            print("\nFigura seleccionada: Cuadrado")
            l = int(input("Anote la medida de un lado de la figura: "))
            area = l * l
        else:
            if opc == 3:
                fig = "círculo"
                print("\nFigura seleccionada: Círculo")
                r = int(input("Anote la medida del radio: "))
                area = (r * r) * 3.1416
            else:
                if opc == 4:
                    fig = "pentágono"
                    print("\nFigura seleccionada: Pentágono")
                    l = int(input("Anote la medida de un lado de la figura: ")) #Perímetro
                    p = l * 5
                    a = int(input("Anote el valor de la apotema: "))
                    area = (p * a) / 2 #Área

    print ("\nEl área del {} es: {}".format(fig, area))