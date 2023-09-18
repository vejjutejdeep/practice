def bubble_sort(arr):

    print(arr)

    for i in range(len(arr)):

        swap = False

        for j in range(0,(len(arr) - i - 1) ):

            if arr[j] > arr[j+1]:

                arr[j],arr[j+1] = arr[j+1],arr[j]

                swap = True

        if not(swap):

            break
    
    print("sorted array" + str(arr))

arr = [14, 5,21,7,0,1,31,7]
bubble_sort(arr)