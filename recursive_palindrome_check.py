str1 = input("Enter a word to be checked: ")
str1 = str1.lower()

def palindromecheck(word):
    if len(word) == 1:
        return True
    elif len(word) == 2:
        return word[0] == word[1]
    else:
        return palindromecheck(word[1:len(word) - 1]) and word[0] == word[len(word) - 1]

if palindromecheck(str1):
    print("It's a Palindrome")
    quit()
print("It's not a Palindrome")