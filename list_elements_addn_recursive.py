numlst = list()
while True:
    inputnum = input("provide a number: ")
    if inputnum == '':
        break
    numlst.append(int(inputnum))

innercount = 0

def listsum(lst, tot, count):
    if count == len(lst):
        return tot
    else:
        if type(lst[count]) == type(list):
            return listsum(lst[count])
        tot = tot + lst[count]
        count = count + 1
        return listsum(lst, tot, count)

total = listsum(numlst, 0, 0)
print("The total is", total)