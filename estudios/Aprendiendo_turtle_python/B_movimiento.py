import turtle

s = turtle.Screen()
t = turtle.Turtle()

#la pantalla se divide en un plano cartesiano, por lo que se maneja con coordenadas X , Y
t.goto(100, 100)
t.goto(-100,100)

#para regresar al home podemos usar una de las siguientes declaraciones
t.goto(0,0)
t.home()

turtle.done()