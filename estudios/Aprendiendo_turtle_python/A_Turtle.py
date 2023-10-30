import turtle

#creamos la pantalla
s = turtle.Screen()

#creamos el cursor en la pantalla creada
t = turtle.Turtle()

#ahora agregamos movimientos
t.backward(100)
t.right(90)
t.forward(100)
t.left(90)

'''''
tambien lo podemos colocar resumido usando:
t.bk(100)
t.rt(90)
t.fw(100)
t.lt(90)
'''

#para que la pantalla no se cierre sola al correr el codigo de dbe colocar:
turtle.done()

