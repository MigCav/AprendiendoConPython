
# abstraccion se refiere a ocultar el proceso que se esta haciendo en cuanto a codigo
# solo entregar la version resumida, es decir, solo entregar lo importante y no mostrar
# todo el proceso que se hace para llegar a ese punto

class automovil():
    def __init__(self):
        self._estado = "apagado"

    def encender(self):
        self._estado = "encendido"
        print("el auto esta encendido")

    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("conduciendo el auto")


mi_auto =   automovil()
mi_auto.conducir()
 

# por ejemplo aqui no se le va a mostrar al usuario que se esta verificando si el automovil esta apagado
# que luego se encienda y luego conduzca, solo pulsa la opcion conducir y listo
# ES OCULTAR TODO EL PROCESO QUE SE DESARROLLA TRAS DEL TELON

