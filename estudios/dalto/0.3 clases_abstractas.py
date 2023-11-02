from abc import ABC, abstractmethod

# las clases abstractas ayudan a "obligar" a usar determinados metodos en las clases a las que heredan
# suelen referirse a clases "plantillas" ya que no pueden ser instanciadas directamente
# se puede decir que es para "obligar" a realizar poliformismo en clases

class persona(ABC):
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre     =   nombre
        self.edad       =   edad
        self.sexo       =   sexo
        self.actividad  =   actividad

    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"hola, me llamo {self.nombre} y tengo {self.edad} años")


class estudiante(persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f"estoy estudiando: {self.actividad}")

class trabajador(persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f"estoy trabajando en el area de: {self.actividad}")

carlos = estudiante("carlos", 29, "masculino", "programacion")

carlos.presentarse()
carlos.hacer_actividad()