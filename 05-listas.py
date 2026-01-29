"""
Las listas:
es una estructura de atos que permite almacenar varios valores en una sola variables.
Las listas pueden contener datos de mismo o distinto tipo y son mutables (se puede modificar)"""

lista2 = [] #Esto es una lista que no tiene nada, pero sirve para señalar que la variable es una lista
numeros = [1,2,3,4,5]
print(numeros)
nombres = ["Ana", "Luis", "Carlos"]
print(nombres)
mezcla = [10, "Hola", 3.5, True]
print(mezcla)

print(nombres[1])
print("|----------------------------------------|")
print(type(mezcla))
#Agregar elementos a la lista
print(nombres)
nombres[1] = "Pedro"
print (nombres)

nombres.append("Juan")
print(nombres)
print(lista2)

lista2.append(1)
lista2.append(5) #Agregar valores a lista2
lista2.append(7)
print(lista2)