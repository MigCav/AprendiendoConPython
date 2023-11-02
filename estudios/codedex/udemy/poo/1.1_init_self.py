# class FabricaTelefonos():
#     marca = "Samsung"

#     def ElaborarHuawei(self):
#         self.marca = "Huawei"

# telefono = FabricaTelefonos()
# telefono.ElaborarHuawei()
# print(telefono.marca)

class FabricaTelefonos():
    def __init__(self , marca , color):
        self.marca = marca
        self.color = color

telefono = FabricaTelefonos('Huawei' , "Azul")
print(telefono.marca)
print(telefono.color)

"""
__init__   es el metodo constructor
self       es para todo metodo hecho por mi, ayuda a globalizar atributos dentro de un metodo de la clase

"""