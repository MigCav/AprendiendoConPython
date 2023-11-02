class gato():
    def sonido(self):
        return "miau"
        
class perro():
    def sonido(self):
        return "guau"
    
#esto trata de polimorfismo, una misma forma de llamar un mismo metodo que esta en distintas clases pero que tiene
# una forma distinta de operar dependiendo de la clase en el que sea llamado
def hacer_sonido(animal):     
    print(animal.sonido())
    
perro = perro()
gato  = gato()

hacer_sonido(gato)
        
        