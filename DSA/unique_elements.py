def unique_elements(arr):

    dic = {}
    
    for i in range(0,len(arr)):

        if arr[i] not in dic.keys():

            dic[arr[i]] = 1

        elif arr[i] in dic.keys():

            # print(arr[i], dic.keys())

            dic[arr[i]] += 1

            return False
    
    return True

def unique_elements2(arr):

    st = set(arr)

    if len(arr) == len(st):

        # print(len(st), len(arr))

        return True
    
    # print(len(st), len(arr))
    
    return False

arr = [1,21,32,1,3]
print(unique_elements(arr))

arr =[1,2,3,4]
print(unique_elements(arr))

arr = [1,1,1,2,2,3,3,4,5]
print(unique_elements(arr))

print("new elements")

arr = [1,21,32,1,3]
print(unique_elements2(arr))

arr =[1,2,3,4]
print(unique_elements2(arr))

arr = [1,1,1,2,2,3,3,4,5]
print(unique_elements2(arr))