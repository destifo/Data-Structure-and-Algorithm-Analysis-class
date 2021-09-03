lst1 =[1, 2, 3, 4, 5,6]

c1 = 0
c2 = -1
def swapper(lst, c1, c2):
    if c1 == len(lst)//2:
        return lst
    else:

        temp = lst[c1]
        lst[c1] = lst[c2]
        lst[c2] = temp
        c1 += 1
        c2 -= 1
        return swapper(lst, c1, c2)

print(swapper(lst1, c1, c2))
#print(lst1[1:-1])

#c1 == len(lst)//2 + 1