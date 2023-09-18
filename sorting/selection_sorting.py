def sorting(arr):

    print(arr)

    for i in range(len(arr)):

        for j in range(len(arr)):

            if arr[i] < arr[j]:

                arr[i],arr[j] = arr[j],arr[i]
    
    print(arr)

    return arr

arr = [34,1,65,2,67,21]

sorting(arr)
