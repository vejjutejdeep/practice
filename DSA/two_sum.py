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


def find_target_dic(arr,t):
    map = {}
    res = []
    for i in range(len(arr)):
        ele2 = t - arr[i]
        if ele2 in map:
            break
        else:
            map[arr[i]] = i
    res.append(map[ele2])
    res.append(i)
    return res


arr = [2,7,11,15]
target = 9
print("result "  , str(find_target(arr, target)))
print("result "  , str(find_target_dic(arr, target)))

arr2 = [3,3]
target2 = 6
print("result "  + str(find_target(arr2, target2)))
print("result "  + str(find_target_dic(arr2, target2)))

arr3 = [0,3,1,5,7]
target3 = 6
print("result "  + str(find_target(arr3, target3)))
print("result "  + str(find_target_dic(arr3, target3)))

arr4 = [3,2,4]
target4 = 6
print("result " + str(find_target(arr4, target4)))
print("result " + str(find_target_dic(arr4, target4)))