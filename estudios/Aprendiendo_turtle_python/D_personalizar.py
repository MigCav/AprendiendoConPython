import turtle

s = turtle.Screen()
t = turtle.Turtle()

#para cambiar el "background"
s.bgcolor("red")

#para modificar el nombre del lienzo
s.title("proyecto1")

#para modificar el tamaño de la tortuga
#en orden de ancho, largo y borde
t.shapesize(10, 5, 2)

#para modificar el color de la tortuga
t.fillcolor("white")

#para cambiar el color del borde de la tortuga y la linea que deja detras
t.pencolor("white")

#tambien se puede modificar colocando primero el color de la tortuga y luego el de la tinta
t.color("green", "blue")

#para cambiar el grosor de la linea
t.pensize(5)


turtle.done()