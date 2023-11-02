class A():
    def __init__(self):
        self.contador = 0
    
    def incrementar(self):
        self.contador += 1
    
    def cuenta(self):
        return self.contador

class B():
    def __init__(self):
        self.__contador = 0
    
    def incrementar(self):
        self.__contador += 1
    
    def cuenta(self):
        return self.__contador

print("Objeto 1")

a = A()
print(a.cuenta())
a.incrementar()
print(a.cuenta())
print(a.contador)   #es de mala practica dejar el atributo sin encapsular y de llamarlo sin unsar el metodo de la funcion

print("Objeto 2")
b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())
print(b.__contador)  #es una forma de encapsular pero no es la correcta

