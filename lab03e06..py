#turtle function


def sqt(x, y):
    import turtle
    bob = turtle.Turtle()
    bob.color(y)

    bob.forward(x)
    bob.right(90)

    bob.forward(x)
    bob.right(90)

    bob.forward(x)
    bob.right(90)

    bob.forward(x)
    bob.right(90)

    turtle.done()

while True:

    try:
        sqlen = float(input("Enter the length of the square:\n"))
        clr = input("Enter the color:\n")
        break
    except:
        print("Invalid input")
        continue

sqt(sqlen, clr)
