nombre    =   "Miguel"
apellido    =   "Cabrera"
edad        =   28
edad2        =   -28
cadena      =   "si tengo una cadena de texto larga como esta puedo cambiar letras"

print(nombre    ,   apellido    ,   edad)

#forma para encadenar variables en un texto (por lo general al traducir en idiomas)
print("mi nombre es {} apellido {} y mi edad es {}" .format (nombre ,   apellido    ,   (edad)))
print("mi nombre es %s apellido %s y mi edad es %d" %(nombre    ,   apellido    ,   edad))

print(cadena.lower())   #Coloca todas las letras en minuscula
print(cadena.upper())   # coloca todas las letras en mayuscula
print(cadena.capitalize())  #coloca solo la primera letra en mayuscula y pasa a minuscula las demas
print(cadena.title())   #la primera letra de cada palabra pasa a ser mayuscula
print(cadena.swapcase())#cambia minusculas a mayusculas y viceversa
print(cadena[: : 2])    #imprime cada 2 espacios
print(cadena[: : -1])   #imprime la cadena de texto a la inversa
reemplazar  =   cadena.replace("a","A") #cambia el valor a modificar por el valor luego de la coma
reemplazar  =   cadena.replace("",",")
#para sacar el valor absoluto en pyton se usa abs()
print(abs(edad))
print(abs(edad2))
#fuera de python se usa el if, punto de inflexion es 0  -.-.-.-.-.-.-   diciendo if numero  >0  else:   numero  <   0

