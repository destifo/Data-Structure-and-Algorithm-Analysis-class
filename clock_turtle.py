import turtle
p = turtle.Turtle()
sec = turtle.Turtle()
minu = turtle.Turtle()
sc = turtle.Screen()
sc.bgcolor("black")
p.pencolor("white")
p.pensize(3)
p.speed(0)
p.hideturtle()
minu.hideturtle()
sec.hideturtle()
text = turtle.Turtle()
text.hideturtle()

def clockhand(turtobj, pensize, pencolor, rotangle, handlength):
    turtobj.pensize(pensize)
    turtobj.pencolor(pencolor)
    turtobj.right(rotangle)
    turtobj.forward(handlength)

def reverse(turtobj, xcord, ycord):
    turtobj.undo()
    turtobj.up()
    turtobj.goto(xcord, ycord)
    turtobj.down()


p.up()
p.goto(0, -200)
p.down()
#p.circle(250)

p.up()
p.goto(0, 50)
sec.goto(0, 50)
minu.goto(0, 50)
p.down()
p.left(90)


for i in range(12):
    p.pencolor("#eeeff8")
    p.pensize(4)
    p.right(30)
    p.up()
    p.forward(210)
    p.down()
    #p.write(i+1, font =('Book Antiqua', 15, 'italic'))
    p.up()
    p.forward(20)
    p.down()
    p.forward(20)
    p.up()
    p.goto(0, 50)
    p.down()

for i in range(60):
    p.pencolor("#4AC5FF")
    p.pensize(2)
    p.right(6)
    p.up()
    p.forward(245)
    p.down()
    p.forward(3)
    p.up()
    p.goto(0, 50)
    p.down()

text.color("white")
text.right(90)
text.up()
text.goto(-250, -250)
text.down()
text.write("Please Go to the console and set the time", font = ('Arial', 20, 'bold'))

print("Hello, We are gonna set the time\n")
hr = int(input("Please enter the hour from your phone:\n"))
minut = int(input("Enter the minute from your phone:\n"))

startangle_minu = 96
startangle_hr = 30

hrangle = startangle_hr - (30 * hr)
minutangle = startangle_minu - (6 * minut)

sec.speed(2)

p.left(hrangle)
minu.left(minutangle)
sec.left(90)

text.clear()
print("\nplease return to the turtle screen and check the time")

for a in range(112):
    clockhand(p, 5, "#9ff7a9", 30, 120)

    for b in range(60):
        clockhand(minu, 3, "#f7ee32", 6, 200)

        for c in range(60):
            clockhand(sec, 2, "red", 6, 200)
            reverse(sec, 0, 50)

        reverse(minu, 0, 50)

    reverse(p, 0, 50)


#p.hideturtle()

turtle.done()
