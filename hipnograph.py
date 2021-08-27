import turtle

p = turtle.Turtle()
bg = turtle.Screen()
bg.bgcolor("black")
p.pencolor("red")
p.penup()
p.goto(0, 200)
p.pendown()
p.speed(0)

x = y = 0

while True:
    p.forward(x)
    p.right(y)
    y+=1
    if x >= 630:
        x = 630
        y = 210
    x+=3
    if y == 500:
        print(x, y)
        break

    p.hideturtle()


exitonclick()
