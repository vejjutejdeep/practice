def is_palindrome(num):

    flag = False

    if num < 0:

        return flag
    
    reverse = 0

    i = len(list(str(num))) - 1

    temp = num
    
    while temp > 0:

        reverse += (temp % 10) * (10 ** i)
        # print(num % 10)
        # print(10**i)
        # print(reverse)

        temp = temp // 10

        i -=1

    print("reversed number %d" %reverse)

    # print(reverse == num)

    if reverse == num: 

        flag = True
    
    return flag

num1 =121
print("original number %d" % num1)
print(is_palindrome(num1))
num2 = -121
print("original number %d" % num2)
print(is_palindrome(num2))
num3 = 10
print("original number %d" % num3)
print(is_palindrome(num3))
num4 = 101
print("original number %d" % num4)
print(is_palindrome(num4))
num5 = 11003
print("original number %d" % num5)
print(is_palindrome(num5))
