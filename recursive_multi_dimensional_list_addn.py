numlst = [1, 2, 3, [4, 5]]

def listsum(lst):
    if len(lst) == 1:
        if type(lst[0]) == type(lst):
            return listsum(lst[0])
        return lst[0]
    else:
        if type(lst[0]) == type(lst):
            return listsum(lst[0])
        return lst[0] + listsum(lst[1:])


total = listsum(numlst)
print("The total is", total)