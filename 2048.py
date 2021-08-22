import random
import copy

def listdisplay(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(lst[i][j], end='\t')
        print()

def row1_merge(row):
    for i in range(len(numlist) - 1):
        for j in range(len(numlist) - 1, 0, -1):
            if row[j - 1] == 0:
                row[j - 1] = row[j]
                row[j] = 0
    for i in range(len(numlist) - 1):
        if row[i] == row[i + 1]:
            row[i] = 2 * row[i]
            row[i + 1] = 0

    for i in range(len(numlist) - 1, 0, -1):
        if row[i - 1] == 0:
            row[i -1] = row[i]
            row[i] = 0
    return row

def mergeAll_left(lst):
    for i in range(len(lst)):
        lst[i] = row1_merge(lst[i])
    return lst

def reverse(row):
    tmplst = []
    for i in range(len(numlist)-1, -1, -1):
        tmplst.append(row[i])
    return tmplst

def merge_right(lst):
    for i in range(len(numlist)):
        lst[i] = reverse(lst[i])
        lst[i] = row1_merge(lst[i])
        lst[i] = reverse(lst[i])
    return lst

def transpose(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if i == j:
                continue
            else:
                tval = lst[i][j]
                lst[i][j] = lst[j][i]
                lst[j][i] = tval
    return lst

def merge_up(lst):
    lst = transpose(lst)
    lst = mergeAll_left(lst)
    lst = transpose(lst)
    return lst

def merge_down(lst):
    lst = transpose(lst)
    lst = merge_right(lst)
    lst = transpose(lst)
    return lst

def numgenerator(lst):
    if random.randint(1, 4) == 4:
        randval = 4
    else:
        randval = 2

    for i in range(len(lst)):
        rand1 = random.randint(0, 3)
        rand2 = random.randint(2, 5) - 2
        for j in range(len(lst)):
            if lst[rand1][rand2] != 0:
                continue
            else:
                lst[rand1][rand2] = randval
                return
def gamewon():
    for row in numlist:
        if 2048 in row:
            return True
        else:
            return False

def gamelost():
    templst1 = copy.deepcopy(numlist)
    templst2 = copy.deepcopy(numlist)
    templst1 = merge_up(templst1)
    if templst1 == templst2:
        templst1 = merge_down(templst1)
        if templst1 == templst2:
            templst1 = merge_right(templst1)
            if templst1 == templst2:
                templst1 = mergeAll_left(templst1)
                if templst1 == templst2:
                    return True
    return False


numlist = list()
for i in range(4):
    sublst = []
    for j in range(4):
        sublst.append(0)
    numlist.append(sublst)

initval = 0
while initval < 2:
    numlist[random.randint(0, len(numlist) - 1)][random.randint(0, len(numlist) - 1)] = 2
    initval +=1

print("This the 2048 game.")
print("press 8 to add rows up")
print("press 2 to add rows down")
print("press 4 to add columns left")
print("press 6 to add columns right")
print("Type 'done' to exit the game")

templst = list()

listdisplay(numlist)
print()
print()

for i in range(len(numlist)):
    for j in range(len(numlist)):
        templst.append(numlist[i][j])

while True:
    direction = input("Enter a direction: ")
    if direction == '8':
        merge_up(numlist)
    elif direction == '2':
        merge_down(numlist)
    elif direction == '4':
        mergeAll_left(numlist)
    elif direction == '6':
        merge_right(numlist)
    elif direction == 'done':
        quit()
    else:
        print("Incorrect input, please try again")
        continue
    templst1 = list()
    for i in range(len(numlist)):
        for j in range(len(numlist)):
            templst1.append(numlist[i][j])

    movesignal = None
    for i in templst:
        for j in templst1:
            if i != j:
                movesignal = 0
                break

    if movesignal is None:
        print("Move isn't possible, try another Move")
        continue

    if gamewon():
        listdisplay(numlist)
        print("Congratulations, You have won")
        break


    if gamelost():
        print("Game Over!")
        listdisplay(numlist)
        break

    numgenerator(numlist)

    print()
    print()
    listdisplay(numlist)
    templst = []
    for i in range(len(numlist)):
        for j in range(len(numlist)):
            templst.append(numlist[i][j])

'''
Estifanos Bireda
UGR/6051/12
Section 03
'''
