str1 = input("Enter bunch of brackets:")
checkcount = dict()
correctorder = str1.sort()
checkcount['['] = 0
checkcount[']'] = 0
checkcount['{'] = 0
checkcount['}'] = 0
checkcount['('] = 0
checkcount[')'] = 0


for letter in str1:
    if str1.index(letter)
        if '[' or ']' or '{' or '}' or '(' or ')' in letter:
            checkcount[letter] = checkcount.get(letter, 0) + 1

print(str1)
if(checkcount['['] == checkcount[']']) and (checkcount['{'] == checkcount['}']) and (checkcount['('] == checkcount[')']):
    print("Correct no of brackets")
else:
    print("wrong no of brackets")
