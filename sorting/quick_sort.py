def quicksort(arr):

    # print(arr)

    l = len(arr)

    if l <= 1:

        return arr
    else :

        # print(l)

        piovt = arr[l//2]

    item_lower = []

    items_upper = []

    for i in range(l):

        if piovt <  arr[i]:

            items_upper.append(arr[i])
        
        if piovt > arr[i]:

            item_lower.append(arr[i])
        
    return quicksort(item_lower) + [piovt] + quicksort(items_upper)

arr = [21,1,54,12,87,100,2]
print("unsorted array " + str(arr))
print("sorted array " + str(quicksort(arr)))