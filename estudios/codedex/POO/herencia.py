"""""
herencia simple
class persona():
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad   = edad
        self.nacionalidad   = nacionalidad
        
    def hablar(self):
        print("estoy hablando")
        
class empleado(persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, sueldo):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo= trabajo
        self.sueldo = sueldo
        
roberto = empleado("roberto", 28, "venezolano", "programador", 600)
"""
"""
#herencia multiple
class persona():
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad   = edad
        self.nacionalidad   = nacionalidad
        
    def hablar(self):
        print("estoy hablando")

class artista():
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return  F"mi habilidad es: {self.habilidad}"
            
        
        
class empleado_artista(persona,artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, trabajo, sueldo):
        persona.__init__(self,nombre, edad, nacionalidad)
        artista.__init__(self, habilidad)
        self.trabajo = trabajo
        self.sueldo = sueldo
        
    def presentarse(self):
        print (f"mi nombre es {self.nombre} tengo {self.edad} años, soy {self.nacionalidad}, mi habilidad es {self.habilidad} y trabajo en {self.trabajo}")
            
        
        
roberto = empleado_artista("roberto", 28, "venezolano", "cantar", "movistar", 600)

roberto.presentarse()

#si queremos saber si es una subclase de otra:
variable = issubclass(empleado_artista, artista)
print(variable)

#si queremos saber si un objeto es instancia de otro:
instancia = isinstance(roberto, empleado_artista)
print(instancia)
"""

"""
el MRO o Metodo de Resolucion de Orden se refiere a un metodo que este en mas de una clase y que se utilice en un objeto
a cual metodo se le dara prioridad

si quiero saber cual es el MRO (metodo de resolucion de orden) se usa el nombre del objeto y luego mro en minuscula
print(d.mro())
"""
"""
si quiero realizar un metodo de una herencia superior, por ejemplo A es heredada de B, C de B, D de C
se usa el siguiente comando 
F.hablar(B)
"""

"""
crea dos clases llamadas personas con atributos de edad y nombre, teniendo un metodo para imprimir ambos atributos; luego
la clase estudiantes que hereda de personas y agrega el atributo de grado, tambien con su metodo para mostrar los atributos
"""

class persona():
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad = edad
        
    def presentar(self):
        return f"mi nombre es {self.nombre} y mi edad es {self.edad} años"
    
class estudiante(persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado= grado
        
    def presentar(self):
        return f"mi nombre es {self.nombre}, mi edad es {self.edad} y curso {self.grado} "
    
manuel = estudiante("Manuel Puerta", 8, "cuarto")
carlos = estudiante("Carlos Arevalo", 10, "sexto")
rigoberto = estudiante("Rigoberto Cardenas", 12, "octavo")
jose = persona("Jose Andrade", 34)

print(jose.presentar())
print(carlos.presentar())
print(rigoberto.presentar())
print(manuel.presentar())


