def computeLCM(number1, number2):

    maxNumber= max(number1, number2)

    while(number1):

        if maxNumber % number1 == 0 and maxNumber % number2 == 0:

            return maxNumber
        
        maxNumber = maxNumber + 1


print(computeLCM(15, 20))
print(computeLCM(54, 24))
print(computeLCM(12, 14))
print(computeLCM(15, 17))