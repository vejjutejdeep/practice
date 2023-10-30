def validParantresis(args):

    vaild = {"{" :"}", "[":"]", "(":")"}

    static = []

    for i in args:

        print(i)

        if i in vaild:

            static.append(i)
        
        elif i not in vaild and len(static) == 0:

            return False
        
        elif (vaild[static[-1]] != i):

            return False

        elif (vaild[static[-1]] == i):

            static.pop(-1)
        
        print(static)
    
    if len(static) != 0:

        return False

    return True
    
    # print(static)

Input = "()"
print(validParantresis(Input))

Input = "(){}[]"
print(validParantresis(Input))

Input = "(]"
print(validParantresis(Input))

Input = "{[]}"
print(validParantresis(Input))

Input = "[([]])"
print(validParantresis(Input))



