idata = input("read the speedometer:\n")
isplimit = input("Enter the speed limit:\n")


try:
    splimit = int(isplimit)
    orgspeed = abs(int(idata))
except:
    print("Invalid input!")
    quit()


speed = orgspeed - splimit


if speed < 5:
    print("You recieve no ticket...this time")
elif speed < 15:
    print ("You recieve a $100 fine.")
elif speed <= 30:
    print ("You recieve a $200 fine.")
else:
    print("You recieve a ticket for a $200 fine, and mandatory curt date.")
