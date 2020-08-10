ntest = int(input("enter the testcases: "))
for i in range(ntest):
    l = int(input("enter the lenght of the array: "))
    nstr = input("enter the string in single line: ").split()
    arr = list(map(int, nstr))
    arr = sorted(arr)
    # print(arr)
    cou = 0
    p1 = 0
    p2 = len(arr) - 2
    while p1 <= len(arr) - 1 and p2 >= 0:
        print(str(p1) + " pointer1 " + str(p2) + " pointer2 ")
        if (arr[p1] + arr[p2]) == arr[p2 + 1]:
            p1 += 1
            p2 -= 1
            cou += 1
        elif (arr[p1] + arr[p2]) > arr[p2 + 1]:
            p2 -= 1
        else:
            p1 += 1
    if cou == 0:
        print(-1)
    else:
        print(cou)
