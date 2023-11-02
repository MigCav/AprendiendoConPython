class persona():
    def __init__(self, nombre, edad):
        self.nombre =   nombre
        self.edad   =   edad


    def __str__ (self):                 #nos devuelve una representacion del objeto en una cadena de texto
        return f"persona (nombre = {self.nombre}, edad = {self.edad})"
    
    def __add__ (self, otro):
        nuevo_valor =   self.edad   +   otro.edad
        return persona(self.nombre + otro.nombre, nuevo_valor)

    
dalto   =   persona("lucas", 24)
pedro   =   persona("pedro", 27)
maria   =   persona("maria", 18)


nueva_persona   =   dalto + pedro + maria

print(nueva_persona.nombre)
print(nueva_persona.edad)
print(nueva_persona)
