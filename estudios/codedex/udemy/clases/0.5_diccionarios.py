
"""
diccionario = {"nombre" : "miguel",    "apellido" : "cabrera", "edad" : 28}
print(diccionario)
diccionario["peso"] =   74      #agregar una nueva clave(llave) y valor
print(diccionario)

print(diccionario["nombre"])    #agrega un valor en especifico al colocarlo en el corchete

diccionario["nombre"]   =   "enrique"   #para cambiar un valor de una clave

diccionario.pop("edad")         #para eliminar una clave y valor del diccionari(se coloca la clave, no la posicion en el diccionario)
print(diccionario)
if variable in diccionario:     #se coloca "in" para saber si está EN diccionario, lista etc
    ...
"""
"""
diccionario.clear() para limpiar todo el diccionario
"""
"""
diccionario.get("nombre")       #metodo para obtener el valor de la llave del diccionario
print(diccionario.get("nombre"))    #se le puede poner el print

diccionario.setdefault(4 , 5)   #para agregar una nueva llave y valor
print(diccionario)

diccionario.update(4 , 50)      #para actualizar el valor de una llave

diccionario2    =   {1 : 2, 2 : 3, 4 : 5}

diccionario.update(diccionario2)     #tambien usado para actualizar un diccionario que absorbe a otro   
print(diccionario)
"""

"""
En el siguiente diccionario se encuentran capitales de los paises en el mundo 
debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais
en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.

{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
"""
""""
paises  =   {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras",
             "Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires",
             "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
pais  =   input("ingrese el pais que quiere saber la capital: ")

if pais.title() in  paises:
    print(paises.get(pais.title()))
else:
    print("este pais no se encuentra")
"""
""""
Con el siguiente diccionario, debes crear un programa que pregunte al usuario por un número 
el programa debe imprimir el jugador al que hace referencia ese número

{

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}
"""
"""
jugadores = {1 : "Casillas", 15 : "Ramos",3 : "Pique", 5 : "Puyol", 11 : "Capdevila",
             14 : "Xabi Alonso",16 : "Busquets", 8 : "Xavi Hernandez",18 : "Pedrito", 6 : "Iniesta",7 : "Villa"}

print("ingresa un numero para escoger al jugador: ")
jugador =   int(input(""))

if jugador in jugadores:
    print(jugadores.get(jugador))
else:
    print("numero erroneo")
"""

