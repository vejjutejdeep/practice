def find_target(arr, t):
    print(arr, t)
    dic ={}
    resu = []
    for i in range(0,len(arr)):

        if t - arr[i] > 0:

            dic = {t - arr[i]: i}

            for j in range(i + 1,len(arr)):

                for keys in dic.keys():

                    if keys == arr[j]:

                        resu.append(dic[keys])
                        resu.append(j)

                        return resu


arr = [2,7,11,15]
target = 9
print("result "  + str(find_target(arr, target)))

arr2 = [3,3]
target2 = 6
print("result "  + str(find_target(arr2, target2)))

arr3 = [0,3,1,5,7]
target3 = 6
print("result "  + str(find_target(arr3, target3)))

arr4 = [3,2,4]
target4 = 6
print("result " + str(find_target(arr4, target4)))