""""
Escribe un programa que pida dos palabras y diga si riman o no. 
Si coinciden las tres últimas letras tiene que decir que riman. 
Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.

rima1   =   input("ingresa el primer verso: ")
rima2   =   input("ingresa el segundo verso: ")

if  rima1[-3: ]  ==  rima2[-3: ]:
    print("si riman")
elif    rima1[-2: ] ==  rima2[-2: ]:
    print("rima solo un poco")
else:
    print("no rima")
"""
""""
Crear un programa que permita al usuario elegir un candidato por el cual votar. 
Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. 
Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje 
“Usted ha votado por el partido [color que corresponda al candidato elegido]”. 
Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.
""" 
"""""  
print("Candidato A por el partido rojo \nCandidato B por el partido verde \Candidato C por el partido azul ")
candidato =   input("¿Por cual candidato deseas votar?: ")
candidato1    =   candidato.upper()
if      candidato1  ==  "A":
    print("has votado por el partido rojo")
elif    candidato1  ==  "B":
    print("has votado por el partido verde")
elif    candidato1  ==  "C":
    print("has votado por el candidato azul")
else:
    print(" subnormal solo tienes 3 putas letras")
"""   
