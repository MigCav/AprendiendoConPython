#la lista puede tener datos iguales, el conjunto no acepta datos repetidos

conjunto1   =   {1, 2, 3, 4, 8, 6, 7}       #al igual que el diccionario pero solo es un valor por ,

conjunto2   =   set[(1, 2, 3, 4, 5, 6, 7)]  #asi se escribe el conjunto con corchetes

conjuntgo3   =   set((1, 2, 3, 8, 5, 6, 7))  #doble parentesis y set al principio

conjunto1.add(20)                           #añade un nuevo valor al conjunto

conjunto1.remove(8)                         #remueve un elemento, se le da el valor a eliminar

num =   conjunto1.pop()                     #elimina y devuelve un elemento aleatorio del conjunto.
print(conjunto1)
print(num)

conjunto1.update()                          #para añadir elementos(interables)

conjunto1.clear()                           #deja el conjunto vacio
