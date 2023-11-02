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
        