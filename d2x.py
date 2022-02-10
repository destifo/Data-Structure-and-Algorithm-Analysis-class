x=int(input("Enter the decimal: "))
n = int(input("Enter n: "))
def d2x(x, n):   
    lst = []
    while(x>0):
        dig=x%n
        lst.append(dig)
        x=x//n
    lst.reverse()
    result = ""
    for item in lst:
        result +=str(item)
    return result

print(d2x(x, n))

