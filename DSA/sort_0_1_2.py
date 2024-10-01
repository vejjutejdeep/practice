def sort_arr(lis):
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for i in lis:
        if i == 0:
            count_0 += 1
        elif i == 1:
            count_1 += 1
        else:
            count_2 += 1
    
    for i in range(count_0):
        lis[i] = 0
    for i in range(count_0,(count_0 + count_1)):
        lis[i] = 1
    for i in range(count_0 + count_1,count_0 + count_1 +count_2):
        lis[i] = 2
    return lis

print(sort_arr([2,0,2,1,1,0]))