class personaje():
    def __init__(self, nombre, fuerza, velocidad, vida):
        self.nombre     =   nombre
        self.fuerza     =   fuerza
        self.velocidad  =   velocidad
        self.vida       =   vida

    def __str__(self):
        return f"{self.nombre} fuerza: {self.fuerza}, velocidad: {self.velocidad}, vida: {self.vida}"
    
    def __add__(self, otro_pj):

        nuevo_nombre    =   self.nombre + "-" + otro_pj.nombre
        nueva_fuerza    =   round(((self.fuerza + otro_pj.fuerza)/2)**1.5)
        nueva_velocidad =   round(((self.velocidad + otro_pj.velocidad)/2)**1.5)
        nueva_vida      =   round(((self.vida + otro_pj.vida)/2)**1.5)
        
        return  personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad, nueva_vida)

goku    =   personaje("goku", 100, 100, 1000)
vegueta =   personaje("vegueta", 99, 99, 1100)
picoro  =   personaje("picoro", 85, 90, 950)
cell    =   personaje("cell", 150, 170, 2000)

gogeta =   goku + vegueta

print(gogeta)