""""
lista   	=   [1, 2, 3, 4, 5, 6, 5, 5, 4]

lista.append(7) #agrega un valor al final de la lista
print(lista)

lista.insert(2 , 2.5)   #agrega en la posicion asignada(numero antes de la coma), un valor cualquiera (dato despues de la coma) 
print(lista)

print(lista.count(4))   #imprime cuantos valores hay iguales al especificado

print(lista.index(5))   #imprime cuantos valores iguales al indicado hay en la lista

print(lista[5])         #imprime la posicion especificada en la lista nombrada

lista.sort()            #ordena la lista de menor a mayor
print(lista)

lista.reverse()          #ordena la lista de mayor a menor
print(lista)

#para cambiar el dato almacenado en una lista se usa la posicion del dato (entre []) como si fuera una variable
lista[3]    =   3.5

lista.pop()             #elimina el ultimo dato de una lista

lista.remove(2)         # elimina el valor, que se encuenta entre los parentesis, dentro de la lista

lista2  =   []
edad    =   int(input("ingresa tu edad: "))
lista2.append(edad)
print(lista2)
"""
"""
En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez 
debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:
[20, 50, "Curso", 'Python', 3.14]
"""
"""
lista   =   [20, 50, "Curso", 'Python', 3.14]
print(lista)
nombre  =   input("¿Cual es tu nombre?: ")
edad    =   int(input("¿Cual es tu edad?: "))
lista.insert(0  ,   nombre)
lista.insert(1  ,   edad)
print(lista)
"""
"""
Escribe una lista que tenga los números de 1 al 10. 
Luego, debes hacer que los datos que están en las posiciones 4, 7 y 9 sean multiplicados por 2
por último, mostrar la lista nueva con los nuevos datos
"""
lista   =   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)

lista[3]    *=  2
lista[6]    *=  2
lista[8]    *=  2
print(lista)
