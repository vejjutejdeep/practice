def sort_arr(lis):
    low = 0
    mid = 0
    high = len(lis) -1
    while mid <= high:
        if lis[mid] == 0:
            lis[low],lis[mid] = lis[mid], lis[low]
            low += 1
            mid += 1
        elif lis[mid] == 1:
            mid += 1
        elif lis[mid] == 2:
            lis[mid],lis[high] = lis[high],lis[mid]
            high -= 1
    return lis

print(sort_arr([2,0,2,1,1,0]))

def sort_arr_0_1(arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        # print(low,high)
        if arr[low] == 1:
            arr[low],arr[high] = arr[high],arr[low]
            high -= 1
        else:
            low += 1
    return arr
print(sort_arr_0_1([1,0,1,0,1,1]))