ages = "\nYour age?\n"
while 1:
    age = input(ages)
    age = int(age)
    if age<3:
        print("Free")
    elif age<=12:
        print("10 dollars")
    else:
        print("15 dollars")