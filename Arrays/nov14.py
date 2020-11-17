test = int(input())
for ele in range(test):
    le, sum1 = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    su = 0
    start = 0
    end = 0
    inl = True
    for ele1 in range(le):
        if su < sum1:
            su += arr[ele1]
        if su == sum1:
            if inl:
                print("true")
                start += 1
                end = ele1 + 1
            if not(inl):
                end = end
            break
        if su > sum1:
            for ele2 in range(le):
                if su == sum1:
                    start = ele2 + 1
                    end = ele1 + 1
                    inl = False
                    break
                if su < sum1:
                    break
                su -= arr[ele2]
    if su == sum1:
        print(str(start) + "," + str(end))
    else:
        print(-1)
