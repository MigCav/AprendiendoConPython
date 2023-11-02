"""""
Un importante negocio de desinfectante líquido realiza descuentos
dependiendo de la cantidad de litros vendidos según la siguiente escala:
a. Si vende menos de 100 litros, no hay descuento.
b. Si vende entre 101 y 300 litros, el descuento es del 10%.
c. Si vende entre 301 y 500 litros, el descuento es del 15%.
d. Finalmente, si la venta es de más de 500 litros, el descuento es del 25%.
Hacer un programa que solicite el ingreso del importe total de la venta y la
cantidad de litros vendidos y calcule y emita el importe con el descuento
aplicado.
ingresar cuanta plata gastó
cantidad de litros vendidos
regresar cuanta plata debe pagar con el descuento

litros  =   int(input("¿Cuantos litros compró el cliente?: "))
dinero  =   int(input("¿Cuanto dinero pago el cliente?"))
if  litros <=   100:
    print("No tiene descuento")
elif    litros >=   101 <=   300:
    print("10% de descuento, nuevo total: ",    dinero  *   0.90  )
elif    litros >=  301 <   500:
    print("15% de descuento, nuevo total: ",    dinero  *   0.85 )
elif    litros >=  500:
    print("25% de descuento, nuevo total: ",    dinero  *   0.75 )
else:
    print("error")
    """
"""""
cantidad_litros    =   int(input("Ingresa cuantos litros se están comprando: "))
precio_litro   =  10
descuento1  =   0.90
descuento2  =   0.85
descuento3  =   0.75
if  cantidad_litros <=   100:
    print(f"El precio es: ", cantidad_litros *   precio_litro,  "no tiene descuento")
elif    cantidad_litros >=   101 <=   300:
    print(f"El precio es: ",    (cantidad_litros *   precio_litro) * descuento1,  "con un 10% de descuento" )
elif    cantidad_litros >=  301 <   500:
    print(f"El precio es: ",    (cantidad_litros    *   precio_litro)   *   descuento2, "con un 15% de descuento")
elif    cantidad_litros >=  500:
    print(f"El precio es: ",    (cantidad_litros *   precio_litro) * descuento3,  "con un 25% de descuento" )
else:
    print("error")
"""

"""""
    Hacer un programa que solicite el ingreso de las notas del primer parcial y del
segundo parcial de una alumna de programación. El programa deberá analizar
las notas y emitir la situación de la alumna según la siguiente escala:
a. Si tiene 8 o más en ambos parciales, emitir “aprobación directa”.
b. Si no tiene 8 o más en ambos pero tiene aprobados ambos parciales (se
aprueba con 6 o más), emitir “rinde examen final”.
c. Si tiene menos de 6 en alguno de los dos parciales, emitir “debe
recuperar”.
El programa debe emitir solo un cartel, el que corresponda.
    
parcial1    =   int(input("Nota del primer parcial: "))
parcial2    =   int(input("Nota del segundo parcial: "))
if  parcial1    >=   8    and     parcial2    >=   8:
    print("no rinde examen final")
elif parcial1   >=   6    and    parcial2    >=   6:
    print("rinde examen final")
else:
    print("toca reparar materia")
"""   
"""""
Hacer un programa para ingresar por teclado la longitud de los tres lados de un
triángulo y que luego determine e informe con un cartel aclaratorio a qué tipo
de triángulo corresponde:
a. Equilátero: cuando los tres lados sean iguales.
b. Isósceles: cuando dos de los tres lados sean iguales.
c. Escaleno: cuando todos los lados sean distintos.    

lado_a  =   int(input("Ingrese primer lado: "))
lado_b  =   int(input("Ingrese segundo lado: "))
lado_c  =   int(input("Ingrese tercer lado: "))

if  lado_a  ==  lado_b  ==  lado_c:
    print("Triangulo equilatero")
elif lado_a   !=  lado_b  ==  lado_c:
    print("Triangulo isósceles")
elif lado_a   ==  lado_b  !=  lado_c:
    print("Triangulo isósceles")
elif lado_a   ==  lado_c  !=  lado_b:
    print("Triangulo isósceles")
elif lado_a   !=  lado_b  !=  lado_c:
    print("Triangulo escaleno")
else:
    print("error")
    
lado_a  =   int(input("Ingrese primer lado: "))
lado_b  =   int(input("Ingrese segundo lado: "))
lado_c  =   int(input("Ingrese tercer lado: "))
if      lado_a   ==  lado_b  and lado_a  ==  lado_c:
    print("Triangulo equilatero")
elif    lado_a   !=  lado_b  and lado_a  ==  lado_c:
    print("Triangulo isósceles")
elif    lado_a   ==  lado_b  and lado_a  !=  lado_c:
    print("Triangulo isósceles")
elif    lado_a   !=  lado_b  and lado_a  !=  lado_c:
    print("Triangulo escaleno")
else:
    print("Error")
    """""
    
"""""
Hacer un programa para ingresar 4 números. Luego analizar e informar por
pantalla si los mismos se encuentran ordenados de forma decreciente. 

valor1  =   int(input("Ingrese el primer valor: "))
valor2  =   int(input("Ingrese el segundo valor: "))
valor3  =   int(input("Ingrese el tercer valor: "))
valor4  =   int(input("Ingrese el cuarto valor: "))

if  valor1  >   valor2  >   valor3  >   valor4:
    print(" estan ordenados de forma decreciente")
else:
    print("no estan ordenados de forma decreciente")
    """""
"""""
El negocio de desinfectante antes mencionado vende además detergente
suelto, y los precios se aplican según la siguiente escala:
a. 25 ARS por litro los primeros 50 litros.
b. 20 ARS por litro si la venta es de 51 a 200 litros.
c. 15 ARS por litro si la venta es de 201 a 500 litros.
d. 10 ARS por litro si la venta es de más de 500 litros.
Además, si paga en efectivo, tiene un adicional del 10% sobre el importe final.
Hacer un programa que solicite la cantidad de litros vendidos y el tipo de pago
(ingresará 1 si paga en efectivo y 0 con cualquier otro medio de pago) y calcule
y emita por pantalla el monto final a abonar por el cliente.
litros
tipo de pago
regresar cuanto paga en total(ojo descuento)


litros  =   int(input("¿Cuantos litros está comprando?: "))
print("Para pago en efectivo presione 0  \nPara pago otros medios de pago presione 1")
tipo_de_pago    =   int(input(""))
descuento       =   0.90
if      tipo_de_pago    ==   0:
    if  litros  <=  50:
        print("El monto a pagar es: ", (litros * 25)    *   descuento)
    elif    litros  >   50  and litros  <=200:
        print("El monto a pagar es: ", (litros * 20)    *   descuento)
    elif    litros  >   200  and litros  <=500:
        print("El monto a pagar es: ", (litros * 20)    *   descuento)
    elif    litros  >   500:
        print("El monto a pagar es: ", (litros * 20)    *   descuento)
elif     tipo_de_pago    ==   1:
    if  litros  <=  50:
        print("El monto a pagar es: ", (litros * 25))
    elif    litros  >   50  and litros  <=200:
        print("El monto a pagar es: ", (litros * 20))
    elif    litros  >   200  and litros  <=500:
        print("El monto a pagar es: ", (litros * 20))
    elif    litros  >   500:
        print("El monto a pagar es: ", (litros * 20))
else:
    print("Error")
    """""
"""""
    Una importante marca de computadoras permite elegir cierta configuración del
equipo a comprar. Para ello existe la siguiente escala de precios:
i5 (1) i7 (2) i9 (3)
8 RAM (1) USD 800 USD 900 USD 1200
16 RAM (2) USD 900 USD 1000 USD 1400
32 RAM (3) USD 1000 USD 1400 USD 2000
Además, el equipo viene con un disco que permite almacenar 500 GB de
información y que se puede ampliar a 1 TB si así lo desea, lo cual tiene un costo
adicional de USD 300.
Hacer un programa que solicite la opción de procesador, la opción de memoria
RAM, y si extiende el disco o no (ingresa 1 para extender y 0 para no extender)
y calcule y emita por pantalla el monto de la máquina seleccionada.

"""""
"""
print("Seleccione el tipo de procesador: \n 1 Para i5.\n 2 para i7.\n 3 para i9.")
procesador  =   int(input(""))
print("Seleccione el tipo de memoria ram: \n 1 Para 8gb.\n 2 para 16gb.\n 3 para 32gb.")
ram     =   int(input(""))
print("¿Desea ampliar el disco duro a 1TB?:\n 0 Si\n 1 No")
ampliacion_disco_duro   =   int(input(""))
disco  =   300

if ampliacion_disco_duro    ==  0:
    if      procesador  ==  1:
        if  ram ==  1:
            print(f"El precio es: ", 800    +   disco )
        elif    ram ==  2:
            print(f"El precio es: ", 900    +   disco )
        elif    ram ==  3:
            print(f"El precio es: ", 1200    +   disco )
        else:
            print("error")
    elif    procesador  ==  2:
        if  ram ==  1:
            print(f"El precio es: ", 900    +   disco )
        elif    ram ==  2:
            print(f"El precio es: ", 1000    +   disco )
        elif    ram ==  3:
            print(f"El precio es: ", 1400    +   disco )
        else:
            print("error")
    elif    procesador  ==  3:
        if  ram ==  1:
            print(f"El precio es: ", 1000    +   disco )
        elif    ram ==  2:
            print(f"El precio es: ", 1400    +   disco )
        elif    ram ==  3:
            print(f"El precio es: ", 2000    +   disco )
        else:
            print("error")
elif ampliacion_disco_duro  ==  1:
    if      procesador  ==  1:
        if  ram ==  1:
            print(f"El precio es: ", 800)
        elif    ram ==  2:
            print(f"El precio es: ", 900)
        elif    ram ==  3:
            print(f"El precio es: ", 1200)
        else:
            print("error")
    elif    procesador  ==  2:
        if  ram ==  1:
            print(f"El precio es: ", 900)
        elif    ram ==  2:
            print(f"El precio es: ", 1000)
        elif    ram ==  3:
            print(f"El precio es: ", 1400)
        else:
            print("error")
    elif    procesador  ==  3:
        if  ram ==  1:
            print(f"El precio es: ", 1000 )
        elif    ram ==  2:
            print(f"El precio es: ", 1400 )
        elif    ram ==  3:
            print(f"El precio es: ", 2000 )
        else:
            print("error")
else:
    print("Error")
"""

"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete, así
que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda.
Cada payaso pesa 112 g y cada muñeca 75 g.
Un cliente frecuente pide la cantidad de 23 payasos y 54 muñecas, 
realiza un programa que muestre el peso total de toda la venta.
"""
"""
cantidad_payasos    =   int(input("¿Cual es la cantidad de payasos?: "))
cantidad_munecas    =   int(input("¿Cual es la cantidad de muñecas?: "))
peso_payaso         =   112
peso_muneca         =   35
print(f"el peso total es: ",    (peso_payaso    *   cantidad_payasos)   +   (peso_muneca    *   cantidad_munecas),  "gramos")
"""
"""""
valor1  =   int(input("ingrese el primer valor: "))
valor2  =   int(input("ingrese el segundo valor: "))
valor3  =   int(input("ingrese el tercer valor: "))

num_ord =   [valor1,valor2,valor3]
sorted_list =   sorted(num_ord)
print(sorted_list)
"""
"""
litros_vendidos = int(input("Ingrese la cantidad de litros vendidos: "))
tipo_pago = int(input("Ingrese el tipo de pago (1 - Efectivo, 0 - Otro medio de pago): "))

precio_por_litro = 0

if litros_vendidos <= 50:
    precio_por_litro = 25
elif litros_vendidos <= 200:
    precio_por_litro = 20
elif litros_vendidos <= 500:
    precio_por_litro = 15
else:
    precio_por_litro = 10

monto_total = litros_vendidos * precio_por_litro

if tipo_pago == 1:  # Pago en efectivo
    monto_total *= 1.1

print("El monto final a abonar es:", monto_total, "ARS")
"""
{}