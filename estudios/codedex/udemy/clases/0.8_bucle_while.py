#el bucle while siempre debe llevar un contador para saber cuando frenar. Dependera del codigo si va al principio de la
#operacion o al final de ésta. Puede ser cualquier variable pero suele usarse "i" o la "j"
""""
Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero


valor   =   int(input("Ingresa un numero para ver su tabla de multiplicar: "))
i=0
while   i   ==  0:
    print(valor,"* 1 =", valor*1)
    print(valor,"* 2 =", valor*2)
    print(valor,"* 3 =", valor*3)
    print(valor,"* 4 =", valor*4)
    print(valor,"* 5 =", valor*5)
    print(valor,"* 6 =", valor*6)
    print(valor,"* 7 =", valor*7)
    print(valor,"* 8 =", valor*8)
    print(valor,"* 9 =", valor*9)
    print(valor,"* 10 =", valor*10)
    i   +=1

valor   =   int(input("Ingresa un numero para ver su tabla de multiplicar: "))
i=0
mult=1
while   i   ==  0:
    i+=1
    print(valor, "*", mult, "=", valor * mult)
    mult +=1
    print(valor, "*", mult, "=", valor * mult)
    mult +=1
    print(valor, "*", mult, "=", valor * mult)
    mult +=1
    print(valor, "*", mult, "=", valor * mult)
    mult +=1
    print(valor, "*", mult, "=", valor * mult)
    mult +=1
    print(valor, "*", mult, "=", valor * mult)
    mult +=1
    print(valor, "*", mult, "=", valor * mult)
    mult +=1
    print(valor, "*", mult, "=", valor * mult)
    mult +=1
    print(valor, "*", mult, "=", valor * mult)
    mult +=1
    print(valor, "*", mult, "=", valor * mult)
    mult +=1
    
valor   =   int(input("Ingresa un numero para ver su tabla de multiplicar: "))
i=0
mult=1
while   i   ==  0:
    i+=1
    print(valor, "*", mult, "=", valor * mult)
    mult+1
    while   mult    <   10:
            mult    +=1    
            print(valor, "*", mult, "=", valor * mult)
          
            
valor   =   int(input("Ingresa un numero para ver su tabla de multiplicar: "))
i=0
while i <10:
    print(valor, "*", i+1, "=", valor*(i+1))
    i += 1

  
Escribir un programa que pregunte al usuario su edad y muestre por pantalla
todos los años que ha cumplido (desde 1 hasta su edad).

edad    =   int(input("¿cual es tu edad?: "))
i       =   0
while i < edad:
    i += 1
    print("Que cumpla:", i)
"""
"""
 Hacer un programa para mostrar los números del 1 al 10. No se debe realizar
ningún pedido de datos. USANDO WHILE.

contador = 0
while contador != 11:
     print(contador)
     contador += 1
 """    
"""
Hacer un programa para mostrar los números del 10 al 1. No se debe realizar
ningún pedido de datos. USANDO WHILE.

contador2 = 10
while contador2 != 0:
    print(contador2)
    contador2 -= 1
"""    
"""
Hacer un programa que solicite la edad de un grupo de personas. El programa
deberá pedir edades hasta que se ingrese una edad menor a 18 años. Deberá
mostrar por pantalla cuántas personas mayores se registraron.
"""
"""
edades = 0
edad = 18
while edad >= 18:
    edad = int(input("ingrese su edad: "))
    if edad >= 18:
        edades += 1
print(edades)
"""
"""
4. Hacer un programa que solicite dos números y luego muestre los números
entre el menor y el mayor de ellos. Acordate, usando While.
"""
"""
num1 = 1
num2 = 1


while num1 != 0 and num2 != 0 :
    
    num1 = int(input("ingresa el primer valor: "))
    num2 = int(input("ingresa el segundo valor: "))
    if num1 < num2 :
        for i in range(num1+1, num2):
            print(i)
    else:
        for i in range(num2+1, num1):
            print(i)
"""
"""
Hacer un programa que muestre los números del 1 al 100 de 5 en 5. Ejemplo:
0, 5, 10, 15, 20.... 100. Usando While.
"""
"""
numeros = 0

while numeros != 105:
    for i in range(0, 105, 5):
        print(i)
        numeros += 5
 """   

"""
Hacer un programa que solicite UN número y luego calcule y emita un cartel
aclaratorio si el mismo es primo o no es primo.
Nota: usando While. Ya lo hicimos con FOR, ahora con While.
"""  
"""  
num = int(input("ingrese el valor: "))

contador = 1
primo    = 0
intentos = 0
while contador < num:
    contador += 1
    if num % contador == 0:
        print("el numero no es primo")
        contador = num
        primo += 1
        break
    elif contador == (num - 1) and primo == 0:
        print("el numero es primo")
       
     
otro metodo de hacerlo (y mas facil, gpt) esta abajo
   
        
numero = int(input("Ingrese un número entero positivo: "))

contador = 2
es_primo = True

while contador < numero:
    if numero % contador == 0:
        es_primo = False
        break
    contador += 1

if es_primo:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
  """    
"""  
Hacer un programa que solicite una lista de números que corta cuando se
ingresa un cero y luego mostrar por pantalla el máximo de ellos y la posición
en la que fue ingresado.
"""
"""  
mayor   =   0
posc    =   0
contador    =   0
num = 1
while num != 0:
    
    num =   int(input("ingresa un numero: "))
    contador += 1
    if num == 0:
        break
    elif num > mayor:
        mayor = num
        posc = contador
    
print("el numero mas alto fue: {} ingresado en la posicion: {}".format(mayor, posc))

"""
"""
Hacer un programa que solicite una lista de números que corta cuando se
ingresa un cero y luego mostrar por pantalla el menor y el segundo menor.
"""
"""
num =   1
valor1 = 0
valor2  = 0
contador = 0

while num != 0:
    num = int(input("ingresa un valor: "))
    
    if num == 0:
        break
    else:
        if contador == 0:
            valor1  =   num
        else:
            if contador == 1:
                if valor1 > num:
                    valor2 = valor1
                    valor1 = num
                else:
                    valor2 = num
            else:
                if valor1>num:
                    valor2 = valor1
                    valor1 = num
                else:
                    if valor2 > num:
                        break
    contador += 1
if contador == 1:
    print(valor1)
else:
    print(valor1)
    print(valor2)
"""
    
"""   
    Realizar el nuevamente el ejercicio 8 pero ahora debe devolver además la
posición en la que fue encontrado cada uno de los mínimos.
"""   
"""
num     =   1
valor1  =   0
valor2  =   0
contador=   0
lugar1  =   0
lugar2  =   0

while num != 0:
    num = int(input("ingresa un valor: "))
    
    if num == 0:
        break
    else:
        if contador == 0:
            valor1  =   num
            lugar1  =   1
        else:
            if contador == 1:
                if valor1 > num:
                    valor2 = valor1
                    valor1 = num
                    lugar1 = 2
                    lugar2 = 1
                else:
                    valor2 = num
                    lugar2 = 2
            else:
                if valor1>num:
                    valor2 = valor1
                    valor1 = num
                    lugar2 = lugar1
                    lugar1 = contador +1
                else:
                    if valor2 > num:
                    
                        break
    contador += 1
if contador == 1:
    
    print(valor1,lugar1)
else:
    print(valor1, lugar1)
    print(valor2, lugar2)
"""

"""
Hacer un programa que solicite una lista de números que corta cuando se
ingresa un cero y luego emitir por pantalla el máximo de los números
negativos y el mínimo de los números positivos.
"""
""""
alto = None
bajo = None
num = 1
contador = 0
while True:
    if num != 0:
        num = int(input("ingrese un valor: "))
        if num > 0:
            if bajo == None:
                bajo = num
            else:
                if bajo > num:
                    bajo = num
        elif num < 0:
            if alto == None:
                alto = num
            else:
               if alto < num:
                   alto = num
    else:
        break
    
if alto != None:
    print(alto)
else:
    print("no se ingreso numero negativo")    
if bajo != None:
    print(bajo)
else:
    print("no se ingresaron numero enteros")
"""
"""
11. Hacer un programa para ingresar una lista de números que corta cuando se
ingresa un cero y luego mostrar: la cantidad de números primos, la cantidad de
números pares, la cantidad de positivos y la cantidad de negativos.
"""

primos      = 0
pares       = 0
negativos   = 0
es_primo    = True
num = 1
while True:
    num =   int(input("ingrese un valor: "))
    if num != 0:
        if num > 0:
            if num % 2  == 0:
                pares   += 1
                es_primo = False
                break
            else:
                if es_primo == True:
                    primos +=1
                else:
                    break
        elif num < 0:
            negativos += 1
    else:
        break
print("numeros primos:", primos)
print("numeros pares:", pares)
print("numeros negarivos:", negativos)w