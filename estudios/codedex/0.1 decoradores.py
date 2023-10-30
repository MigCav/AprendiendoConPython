class persona():
    def __init__(self, nombre, edad):
        
        self.__nombre = nombre
        self.__edad   = edad

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new__nombre):
        self.__nombre   = new__nombre

    
dalto = persona("lucas", 29)

nombre = dalto.nombre
print(nombre)

dalto.nombre = "pepe"
nombre  = dalto.nombre
print(nombre)

