#spirograph
import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(15)

for i in range(100):
    for colours in ["red", "yellow", "magenta", "blue", "cyan", "green", "violet", "white"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)

turtle.hideturtle()
turtle.done(d)
