#turtle spiral
import turtle
fibo = turtle.Turtle()

for i in  range(50):
    fibo.circle(10 * i)
    fibo.up()
    fibo.sety((10 * i)*(-1))
    fibo.down()

turtle.done()
