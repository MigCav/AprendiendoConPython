"""""
Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, 
imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""
"""
class Estudiante():
    def __init__(self, _nombre, _nota):
        self._nombre = _nombre
        self._nota = _nota
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def nota(self):
        return self._nota
    
    def promedio(self):
        print("Nombre: {} \nNota: {}".format(self._nombre, self._nota))
        if self._nota >= 5:
            print("el alumno ha aprobado")
        else:
            print("el alumno ha reprobado")
            
cabrera = Estudiante("Miguel Cabrera", 7)

cabrera.promedio()

"""
"""""
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. 
Calcular después la suma, resta, multiplicación y división. 
Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.
"""
"""
class calculadora():
    def __init__(self):
        self._valor1 = int(input("ingrese el valor 1: "))
        self._valor2 = int(input("ingrese el valor 2: "))
        
    def sumar(self):
        self.resultado = self._valor1 + self._valor2
        return(self.resultado)
        
    def restar(self):
        resultado_resta = self._valor1 - self._valor2
        return(resultado_resta)
        
    def multiplicar(self):
        resultado_multiplicacion = self._valor1 * self._valor2
        return(resultado_multiplicacion)
        
    def dividir(self):
        resultado_division = self._valor1 / self._valor2
        return(resultado_division)
        

calcular = calculadora()
suma = calcular.sumar()
resta = calcular.restar()
multiplicacion = calcular.multiplicar()
division = calcular.dividir()
print(suma)
"""
"""
Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; 
luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro.
Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes.
Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno
"""

class fabrica():
    def __init__(self, _llantas, _color, _precio):
        self._llantas = _llantas
        self._color = _color
        self._precio = _precio
    
    @property   
    def llantas(self):
        return self._llantas
    
    @property
    def color(self):
        return self._color
    
    @property
    def precio(self):
        return self._precio
    
class motos(fabrica):
    def datos(self):
        print("La cantidad de neumaticos es de :", self._llantas)
        print("El color del vehiculo es: ", self._color)
        print("el precio del vehiculo es de: ",self._precio)
class carros(fabrica):
    def datos(self):
        print("La cantidad de neumaticos es de :", self._llantas)
        print("El color del vehiculo es: ", self._color)
        print("el precio del vehiculo es de: ",self._precio)
    
    
    
       
br200 = motos(2, "negro", 1500)
superdt = motos(2, "azul", 2000)
aveo = carros(4, "azul marino", 4500)
corsa = carros(4, "blanco", 3500)

br200.datos()
