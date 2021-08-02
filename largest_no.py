# Finding the largest no in a list of numbers
clist = {10, 5, 56, 89, 5000, 2, 99}
m = 0
for i in clist:
    if i > m:
        m = i
        continue
print(m)
