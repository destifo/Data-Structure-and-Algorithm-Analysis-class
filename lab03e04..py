#grade program
while True:
    try:
        avg = float(input("Enter your remark:\n")
        while True:
            if avg > 100 or avg < 0:
                print("You entered an incorrect score, please enter a no between  and 100")
                continue
        break
    except:
        print("Invalid input!\nPlease Enter a numeric value.")
        continue

if avg >= 85:
    print('A')
elif avg >= 70:
    print('B')
elif avg >= 50:
    print('C')
elif avg >= 40:
    print('D')
else:
    print('F')
