from django.db import models

# Create your models here.

class clientes(models.Model):
    nombre = models.CharField(max_length=30) #charfield para indicar que voy a ingresar texto
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True) #emailfield valida que sea un correo el ingresado, con su @ y punto
    tlfno = models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.nombre
    
class articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField() #para especificar que se ingresara un entero
    def __str__(self) -> str:
        return self.nombre
    
    
class pedidos(models.Model):
    numero = models.IntegerField()

    fecha = models.DateField()    #para ingresar fechas
    entregado = models.BooleanField() #para ingresar booleanos