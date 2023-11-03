def ifNumber(number):

    if len(number) > 1:

        return number[1:].isdigit()
    else:

        return number.isdigit()

def computerArray(arr):

    number = []

    for iter in arr:

        check = ifNumber(iter)

        if check:

            number.append(iter)

        else:

            ope1 = int(number.pop(-1))

            ope2 = int(number.pop(-1))

            operation = { "+" :lambda ope1, ope2: ope1+ope2, 
                         "-" : lambda ope1, ope2: ope1-ope2, 
                         "*": lambda ope1, ope2: ope1*ope2, 
                         "/": lambda ope1, ope2: ope1/ope2}
            
            if operation[iter] == "/" and min(ope1,ope2) == 0:

                number.append[0]
            
            else:
                result  = operation[iter](ope2, ope1)

                number.append(result)
            
        # print(number)

    return int(number[0])

tokens = ["2","1","+","3","*"]
print("answer " + str(computerArray(tokens)))

tokens = ["4","13","5","/","+"]
print("answer " + str(computerArray(tokens)))

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print("answer " + str(computerArray(tokens)))

tokens = ["0","3","/"]
print("answer " + str(computerArray(tokens)))

tokens = ["3","11","5","+","-"]
print("answer " + str(computerArray(tokens)))