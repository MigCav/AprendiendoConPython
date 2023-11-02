"""
def <nombre de la funcion>():
    <funcion>
""" 
"""
def tabla7():
    for i in range(11):
        print("7 x {} = {}". format(i, i*7))
        
tabla7()   
"""
"""
Crear un programa que tenga una lista
luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista.
Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas
"""
"""
lista   =   []

def agregar():
    lista.append(int(input("agregue un numero a la lista: ")))
    lista.append(int(input("agregue un numero a la lista: ")))

agregar()
agregar()
agregar()
agregar()
print(lista)

listapares      =   []
listaimpares    =   []

def debanado():
    lista.sort()
    for i in lista:
        if i    %   2   ==  0:
            listapares.append(i)
        else:
            listaimpares.append(i)

debanado()
print(listaimpares)
print(listapares)
print(lista)
""" 
"""   
Escribir una función que reciba un número entero positivo y devuelva su factorial.    
"""
"""
def factorial():
    numero  = int(input("ingrese un valor entero positivo: "))
    contador = 1
    for i in range(numero,0,-1):
            contador *= i
    
    print(contador)
    
factorial()
"""
"""
num = int(input("agrega un num: "))
var = 0
for i in range(1, num):
    if i * i == num:
        var = i
        print(var)
        break
else:
    print("n")
"""
"""
crear una funcion que pida dos numeros, si el primero es mayo al segundo, mostrar 1
si el segundo es mayor al primero mostrar -1
si son iguales mostrar 0
"""
"""
def numeros():
    num1    =   float(input("ingresa el primer valor: "))
    num2    =   float(input("ingresa el segundo valor: "))
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0
    
print (numeros())
"""
"""
escribir una funcion que calcule el total de una factura tras aplicarle el IVA
debe recibir la cantidad sin IVA y luego el % de IVA a aplicar
si no recibe un % de iva debe aplicar automaticamente el 21%
"""
"""
def factura():
    monto   = float(input("ingrese el monto: "))
    iva     = float(input("ingresa el {} del iva: ".format("%")))
    total   = 0
    if iva > 0:
       total   = monto + ((monto * iva) / 100) 
    else:
        iva = 21
        total   = monto + ((monto * iva) / 100)
    return total

print("el monto a pagar es: ",factura())   
"""      
"""
Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura
y la otra el area de un circulo con argumento de radio
"""
"""
def area_cuadrado(area): 
    return (area * area)
def area_circulo(radio):
    area2 = 3.1416 * (radio * radio)
    return area2
print(area_cuadrado(7))
print(area_circulo(10))
"""
"""
Escribir una función que reciba una muestra de números en una lista y devuelva su medida.
"""
def muestra():
    listanum    =  []
    i           =   0
    num = 1
    while i == 0:
        if num != 0:
            num = float(input("ingrese numeros a la lista"))
            listanum.append(num)
        else:
            i +1
    return len(listanum)
print(muestra())    
    