"Lesson 21 - Loop for"



for i in range(1000):
    if (i%5 == 0 and i%7 == 0 and i%9 == 0):
        print(i, "is divisible by 5, 7 and 9")
    elif (i%5 == 0 and i%7 == 0):
        print(i, "is divisible by 5 and 7")
    elif (i%5 == 0 and i%9 == 0):
        print(i, "is divisible by 5 and 9")
    elif (i%7 == 0 and i%9 == 0):
        print(i, "is divisible by 7 and 9")
    elif (i%5 == 0):
        print(i, "is divisible by 5")
    elif (i%7 == 0):
        print(i, "is divisible by 7")
    elif (i%9 == 0):
        print(i, "is divisible by 9")
    elif (i%5 != 0 or i%7 != 0 or i%9 != 0):
        print(i, "is not divisible by 5, 7 or 9")




