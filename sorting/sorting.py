def sorting(arr):

    print(arr)

    for i in range(len(arr)):

        print(arr[i])

        temp = 0

        for j in range(len(arr)):

            if arr[i] >= arr[j]:

                temp = arr[i]

                arr[j] = arr[i]

                arr[j] = temp
        
        print(arr)

    return arr

arr = [34,1,65,2,67,21]

sorting(arr)
