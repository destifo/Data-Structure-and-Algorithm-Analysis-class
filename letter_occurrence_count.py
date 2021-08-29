
def countstr(Str):
    global letter
    ctr = dict()
    for letter in Str:
        if letter in ctr:
            ctr[letter] = ctr[letter] + 1
        else:
            ctr[letter] = 1
    #another way is 
    #ctr[letter] = ctr.get(letter, 0)
    for k,v in ctr.items():
        print("The occurrence of", k, "is", v, "times")


Str1 = input("Please Enter the word:\n")
countstr(Str1)
