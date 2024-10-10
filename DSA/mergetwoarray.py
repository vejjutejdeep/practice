def merge(arr1, arr2):

    left = len(arr1) - 1
    right = 0

    while left >= 0 and right < len(arr2):
        if arr1[left] > arr2[right]:
            arr1[left],arr2[right] = arr2[right],arr1[left]
            left -= 1
            right += 1
        else:
            break
    arr1.sort()
    arr2.sort()
    arr1 = arr1 + arr2
    return arr1

arr1 = [3,5,7]
arr2 = [1,4,9,10]
print(merge(arr1,arr2))
arr1 = [1,4,8,10] 
arr2 = [2,3,9]
print(merge(arr1,arr2))
arr1 = [0,2,6,8,9]
arr2 = [1,3,5,7]
print(merge(arr1,arr2))