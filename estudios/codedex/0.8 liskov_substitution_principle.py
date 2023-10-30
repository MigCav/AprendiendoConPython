#Una subclase deba hacer Todo lo que hace la clase madre, de no ser asi hay que replantearlo como abajo
#Definiendo todo lo que tienen en comun con una sola clase y luego otra clase que separe lo que hace cada ave por separado

class ave():
    pass

class ave_voladora(ave):
    print("Estoy volando")


class ave_nadadora(ave):
    print("Estoy nadando")
