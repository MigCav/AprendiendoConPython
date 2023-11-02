"""""
for i in range(1, 10, 2):              #primer valor inicia el conteo, segundo es el limite, tercero cada cuanto va a tomar el valor
    print(i)                           # al ser 2 toma 1 valor no y el 2do si, 3ro no 4to si
#si el tercer valor fuera 3 ignora dos y toma el 3ro, ignora 2 y toma el 6to

lista = [9, 8, 7, 6, 5]                
for i in lista:                        #para mostrar la lista de manera vertical
    print(i)
"""  
""""" 
Imprimir por pantalla los numeros del 1 al 10, luego
pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras
""" 

""" 
for i in range(1,11):
    print(i)
num1    =   int(input("ingresa el primer valor: "))
num2    =   int(input("ingresa el segundo valor: "))
if num1 <= num2:
    for i in range(num1, num2+1):
        print(i)
else:
    for i in range(num2,num1+1):
        print(i)
"""
"""
numeros =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in numeros:
    print(i)
num_1   =   int(input("ingrese el primer valor: "))
num_2   =   int(input("ingrese el segundo valor: "))
if num_1 in numeros and num_2 in numeros:
    if num_1 < num_2:
        print(numeros[num_1-1: num_2])
    elif num_2 < num_1:
        print(numeros[num_2-1 : num_1])
else:
    print("el rango entre numeros es erroneo")
 """   
""""
 Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números
 pero solo imprimiendo los números que sean impares
"""
"""
num1 = int(input("ingrese el primer valor: ")) 
num2 = int(input("ingrese el segundo valor: ")) 

if num1 >= num2: 
    for i in range(num2, num1): 
        if i % 2 != 0:
            print(i)
else:
    for i in range(num1, num2):
        if i % 2 != 0:
            print(i)
"""
"""
Hacer un programa que solicite UN número y luego calcule y emita un cartel
aclaratorio si el mismo es primo o no es primo.
Nota: un numero es primo cuando es divisible únicamente por 1 y por sí
mismo.
"""
"""  
num1 = int(input("ingresa el valor:"))

for i in range(2, num1):
    if num1 % i ==0:
        print("el numero no es primo")
        break
else:
    print("el numero es primo")

  """    
    
"""    
num = int(input("Ingrese un número: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "NO es un número primo")
            break
    else:
        print(num, "es un número primo")
else:
    print(num, "NO es un número primo")
"""  
"""  
lista   =   [11,12,13,14,15,16]
for i in lista:
    print(i)
"""
"""
Hacer un programa que solicite 10 números y luego mostrar por pantalla el
máximo de ellos y la posición en la que fue ingresado.

posicion = 0
maximo  =   0
for i in range(10):
    n   =   int(input("ingresa un valor: "))
    if n > maximo:
        maximo      =   n
        posicion    =   i
else:
    print("el numero mas alto es {} y la posicion fue {}".format(maximo,posicion))
"""   
"""
Hacer un programa que solicite 20 edades y luego calcule el promedio de edad
de aquellas personas mayores a 18 años.

edades  =   0
promedio    =   0


for i in range(20):
    edad  =   int(input("ingresa las edades: "))
    if edad > 18:
        promedio +=1
        edades   += edad
print("El promedio de edad entre los mayores de 18 es de: {}".format(edades / promedio))
"""
"""   
Hacer un programa que solicite 20 números y luego emitir por pantalla el
máximo de los números pares y el mínimo de los números impares.

paralto =   0
imparbajo   =   0
bp = 0
bi = 0

for i in range(10):
    numero  =   int(input("ingrese el valor: "))
    if numero % 2 == 0:
        if bp == 0:
            paralto = numero
        elif numero > paralto == True:
            paralto = numero
    elif numero % 2 != 0:
        if bi == 0:
            imparbajo = numero
        elif imparbajo > numero == True:
            imparbajo = numero
            
print("el numero par mas alto es: {} y el impar mas bajo es: {}".format(paralto, imparbajo))
"""
"""
Hacer un programa para ingresar 10 números y luego calcule y emita el mayor
de los primos de la lista. En caso de no haber ningún número primo, deberá
aclararlo con un cartel.
"""
"""
numprimo = 0

for i in range(10):
    num = int(input("ingresa un valor: "))
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        if numprimo < num:
            numprimo = num
if numprimo == 0:
    print("no hay ningun numero primo entre los valores")
else:
    print(numprimo)
"""
num = int(input("ingresa:" ))
print(num)        