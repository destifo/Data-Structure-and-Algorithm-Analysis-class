import turtle
wb = turtle.Turtle()

wb.speed(10)
wb.color("red", "yellow")
wb.begin_fill()

for i in range(50):
    wb.left(170)
    wb.forward(300)

wb.end_fill()

turtle.done()
