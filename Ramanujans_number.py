#This program searches for numbers that are ramanujuan's number


def calramanaujuan(interval):
    for i in range(interval):
        for j in range(interval):
            for k in range(interval):
                for l in range(interval):
                    if i == k or i == j or i == l or j == k or j == l or k == l or (i** 3) + (j**3) != (k**3 + l**3):
                        continue
                    else:
                        print(i, j, k, l)
                        break
number = int(input("Enter the interval:\n"))         
calramanaujuan(number)