ntest = int(input("enter the testcases: "))
for i in range(ntest):
    l = int(input("enter the lenght of the array: "))
    nstr = input("enter the string in single line: ").split()
    arr = list(map(int, nstr))
    # print(arr)
    cou = 0
    for el2 in range(len(arr) - 1):
        for ele in range(el2 + 1, len(arr)):
            if arr[ele] + arr[el2] in arr:
                cou += 1
    if cou == 0:
        print(-1)
    else:
        print(cou)
