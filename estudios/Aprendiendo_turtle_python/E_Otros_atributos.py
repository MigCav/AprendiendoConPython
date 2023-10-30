import turtle

s = turtle.Screen()
t = turtle.Turtle()

#para hacer una figura y rellenarla
#todo el codigo que este entre el principio y el final sera el rellenado
t.begin_fill()
#podemos colocar el color qeu queremos que sea antes de cada figura
t.color("red", "blue")
t.circle(50)
t.end_fill()


#puedes cambiar la figura
t.shape("circle")
t.shape("triangle")
t.shape("clasic")
t.shape("turtle")

#para dejar de "pintar"
t.penup()
t.fd(50)
t.pendown()
t.bk(50)

#regresa la ultima accion (como un control + Z)
t.undo()

#para limpiar la pantalla con la tortuga en el mismo sitio
t.clear()

#para reiniciar
t.reset()


#para dejar una copia en un sitio
t.stamp()

turtle.done()