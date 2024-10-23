def power(x,n):

    ans = 1
    nn = n
    while nn > 0:
        if nn % 2 == 0:
            x = x * x
            nn = nn // 2
        else:
            ans = ans * x
            nn = nn - 1

    if n < 0:
        ans = 1 / ans
    return ans
x = 2.10000
n = 3
print(power(x,n))
x = 2
n = 10
print(power(x,n))