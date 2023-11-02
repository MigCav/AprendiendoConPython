#es una "lista" que NO SE PUEDE MODIFICAR!!!
""""
tupla   =   (1, 2, 3, 4, 5, 6)                  #mejor esta forma para buena practica
tupla   =   1, 2, 3, 4, 5, 6                    #se puede presentar de esta forma tambien

print(tupla[2])                                 #empieza a contar desde 0 igualmente
print(tupla[0 : 3])                             #mismos debanados ya vistos


Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado
es el mes que debe mostrar en la tupla


tupla   =   ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
            "agosto", "septiembre", "octubre", "noviembre", "diciembre")

mes =   int(input("ingrese el mes del año que desea ver: ")) 

if mes >= 1 and mes <= 12:
    print(tupla[mes - 1])
else:
    print("solo existen 12 meses")
    """
"""
Escribir una tupla que tenga las letras del alfabeto. 
Luego, debes pedir al usuario un número, el que haya ingresado
es la letra que debe imprimir el programa
"""
