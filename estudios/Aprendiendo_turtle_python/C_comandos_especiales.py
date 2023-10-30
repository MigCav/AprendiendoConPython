import turtle

s = turtle.Screen()
t = turtle.Turtle()

#para cambiar la velocidad de mov de la tortuga en un rango de 1 al 10
t.speed(5)
t.cicle(20)

#para ocultar a la tortuga
t.hideturtle()
t.circle(30)

#para volver a mostrar a la tortuga
t.showturtle()

#para hacer un circulo relleno, entre los () va el tamaño de este
t.dot(10)

#para moverse en el eje X manteniendo Y sin modificar
t.setx(100)

#para moverse en el eje Y manteniendo X sin modificar
t.sety(100)


turtle.done()