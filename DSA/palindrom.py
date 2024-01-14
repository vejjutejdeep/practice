def is_palindrome(num):

    flag = False

    if num < 0:

        return flag
    
    reverse = 0

    i = len(list(str(num))) - 1

    temp = num
    
    while temp > 0:

        reverse += (temp % 10) * (10 ** i)

        temp = temp // 10

        i -=1

    print("reversed number %d" %reverse)

    # print(reverse == num)

    if reverse == num: 

        flag = True
    
    return flag

def Palidrome2(num):

    negitive = False

    stringnum = str(num)

    if stringnum[0] == '-':

        negitive = True

        stringnum = stringnum[1:]

    num = list(map(int, stringnum))

    print(num)

num1 =121
print("original number %d" % num1)
print(is_palindrome(num1))
print(Palidrome2(num1))

num2 = -121
print("original number %d" % num2)
print(is_palindrome(num2))
print(Palidrome2(num2))

num3 = 10
print("original number %d" % num3)
print(is_palindrome(num3))

num4 = 101
print("original number %d" % num4)
print(is_palindrome(num4))

num5 = 11003
print("original number %d" % num5)
print(is_palindrome(num5))
