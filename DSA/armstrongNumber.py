def isArmstrong(number):

    arr = list(map(int, str(number)))

    lenght = len(arr)

    addtion = 0

    print(arr)

    for i in arr:

        addtion += int(i) ** lenght
    
    print(addtion)

    if addtion == number:

        print("the number is as armstrong number.")
    else:
        print("the number is not a armstrong number.")

isArmstrong(112)
isArmstrong(1122)
isArmstrong(1122)
isArmstrong(153)
isArmstrong(1634)
