#check if any word is a plaindrome or not

def palicheck(str1):
    for i in range(len(str1)):
        if str1[i] != str1[-1 + (i * -1)]:
            return False

    return True

wordcheck = input("Enter the word:\n")
print(palicheck(wordcheck))
