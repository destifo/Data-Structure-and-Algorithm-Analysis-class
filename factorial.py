#factorial
def fac(x):
    y = 1
    for i in range(1, x+1):
        y = i*y

    return y

num = int(input("Enter a positive integer:\n"))
fa = fac(num)

print("The factorial of", num, "is", fa)
